// Handles related-objects functionality: lookup link for raw_id_fields
// and Add Another links.

function html_unescape(text) {
    // Unescape a string that was escaped using django.utils.html.escape.
    text = text.replace(/&lt;/g, '<');
    text = text.replace(/&gt;/g, '>');
    text = text.replace(/&quot;/g, '"');
    text = text.replace(/&#39;/g, "'");
    text = text.replace(/&amp;/g, '&');
    return text;
}

// IE doesn't accept periods or dashes in the window name, but the element IDs
// we use to generate popup window names may contain them, therefore we map them
// to allowed characters in a reversible way so that we can locate the correct 
// element when the popup window is dismissed.
function id_to_windowname(text) {
    text = text.replace(/\./g, '__dot__');
    text = text.replace(/\-/g, '__dash__');
    return text;
}

function windowname_to_id(text) {
    text = text.replace(/__dot__/g, '.');
    text = text.replace(/__dash__/g, '-');
    return text;
}

function showRelatedObjectLookupPopup(triggeringLink) {
    var name = triggeringLink.id.replace(/^lookup_/, '');
    name = id_to_windowname(name);
    var href;
    if (triggeringLink.href.search(/\?/) >= 0) {
        href = triggeringLink.href + '&pop=1';
    } else {
        href = triggeringLink.href + '?pop=1';
    }
    var win = window.open(href, name, 'height=400,width=1000,resizable=yes,scrollbars=yes');
//    var win = window.open(href, name, 'height=500,width=1000,resizable=yes,scrollbars=yes');
    win.focus();
    return false;
}

function dismissRelatedLookupPopup(win, chosenId) {
    var name = windowname_to_id(win.name);
    var elem = document.getElementById(name);
    if (elem.className.indexOf('vManyToManyRawIdAdminField') != -1 && elem.value) {
        elem.value += ',' + chosenId;
    } else {
        document.getElementById(name).value = chosenId;
        //add hebin
        var input = $("#" + name);
        input.trigger("updateEvent",["name","val2"]);
        $("td.field-id>input").trigger("updateEvent",["val1","val2"]);
        //end
    }
    win.close();
}

function showAddAnotherPopup(triggeringLink) {
    var name = triggeringLink.id.replace(/^add_/, '');
    name = id_to_windowname(name);
    href = triggeringLink.href
    if (href.indexOf('?') == -1) {
        href += '?_popup=1';
    } else {
        href  += '&_popup=1';
    }
//    var win = window.open(href, name, 'height=500,width=800,resizable=yes,scrollbars=yes');
//    showModalDialog
    var win = window.open(href, name, 'height=400,width=1000,resizable=yes,scrollbars=yes');    
//    var win = window.showModalDialog(href, name, 'height=400,width=1000,resizable=yes,scrollbars=yes');  
    win.focus();
    return false;
}

function dismissAddAnotherPopup(win, newId, newRepr) {
    // newId and newRepr are expected to have previously been escaped by
    // django.utils.html.escape.
    newId = html_unescape(newId);
    newRepr = html_unescape(newRepr);
    var name = windowname_to_id(win.name);
    var elem = document.getElementById(name);
    if (elem) {
        var elemName = elem.nodeName.toUpperCase();
        if (elemName == 'SELECT') {
            var o = new Option(newRepr, newId);
            elem.options[elem.options.length] = o;
            o.selected = true;
            //elem.trigger("onchange"); //hebin
            //elem.customer_sel_change(name);
        } else if (elemName == 'INPUT') {
            if (elem.className.indexOf('vManyToManyRawIdAdminField') != -1 && elem.value) {
                elem.value += ',' + newId;
            } else {
                elem.value = newId;
            }
        }
    } else {
        var toId = name + "_to";
        elem = document.getElementById(toId);
        var o = new Option(newRepr, newId);
        SelectBox.add_to_cache(toId, o);
        SelectBox.redisplay(toId);
    }
    win.close();
}

function dismissAddAnotherPopupForLinkObj(win,newId, newRepr, array) {
    // newId and newRepr are expected to have previously been escaped by
    // django.utils.html.escape.

    newId = html_unescape(newId);
    newRepr = html_unescape(newRepr);
    var name = windowname_to_id(win.name);
    
    var elem = document.getElementById(name);
//add hebin
    var init_value = elem.value;
//end hebin

    var parent = $("#"+name).parent();
    var next = parent.next();
    
    if (elem) {
        var elemName = elem.nodeName.toUpperCase();
        if (elemName == 'SELECT') {
            var o = new Option(newRepr, newId);
            elem.options[elem.options.length] = o;
            o.selected = true;
        } else if (elemName == 'INPUT') {
            if (elem.className.indexOf('vManyToManyRawIdAdminField') != -1 && elem.value) {
                elem.value += ',' + newId;
            } else {
                elem.value = newId;
//add hebin - for other elem
                var param_id = '';
                var conn, conn1;
                for(var i=0 ; i<array.length; i+=2){
                    
                    param_id = name;
                    conn = "-";  conn1 = array[i]; conn = conn.concat(conn1)
                    param_id = param_id.replace("-id", conn); //shouble be more flexible, extract the info automaticlly , then we're not restricted to "id"
                    var el= document.getElementById(param_id);
                    if(el){
                        el.value = array[i+1];
                    }
                    
                    next.text(array[i+1]);
                    next = next.next();
                }
                if("" == init_value){
                    modify_a(elem);
                }
//end add
            }
        }
    } else {
        var toId = name + "_to";
        elem = document.getElementById(toId);
        var o = new Option(newRepr, newId);
        SelectBox.add_to_cache(toId, o);
        SelectBox.redisplay(toId);
    }
    win.close();
}


function modify_a(el){

    var str;                    
    var obj_id =el.value;
    if(obj_id != ''){
        var a = $(el).prev("a");
        if(a.length > 0){
            a = a[0];
            var href = a.href;
            href = href.replace("/add/","/"+obj_id+"/");
            a.href = href;
            var img = a.innerHTML;
            img = img.replace("icon_addlink.gif","icon_changelink.gif");
            $(a).html(img);
        }
    }

}



