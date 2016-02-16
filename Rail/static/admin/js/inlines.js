/**
 * Django admin inlines
 *
 * Based on jQuery Formset 1.1
 * @author Stanislaus Madueke (stan DOT madueke AT gmail DOT com)
 * @requires jQuery 1.2.6 or later
 *
 * Copyright (c) 2009, Stanislaus Madueke
 * All rights reserved.
 *
 * Spiced up with Code from Zain Memon's GSoC project 2009
 * and modified for Django by Jannis Leidel, Travis Swicegood and Julien Phalip.
 *
 * Licensed under the New BSD License
 * See: http://www.opensource.org/licenses/bsd-license.php
 */
(function($) {
  $.fn.formset = function(opts) {
    var options = $.extend({}, $.fn.formset.defaults, opts);
    var $this = $(this);
    var $parent = $this.parent();

/**************************************************************************************************

                   " updateElementIndex "  function

***************************************************************************************************/
    
    var updateElementIndex = function(el, prefix, ndx) {
//modify hebin        
      var id_regex = new RegExp("(" + prefix + "-(\\d+|__prefix__))");
//      var id_regex = new RegExp("(" + prefix + "-(\\d+|__prefix__|empty))");  //not need to modify
//end modify
      var replacement = prefix + "-" + ndx;
      if ($(el).attr("for")) {
        $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
      }
      if (el.id) {
        el.id = el.id.replace(id_regex, replacement);
        
//add hebin
        if(options.isLink == "True"){
            var a = $(el).prev("a");
            if(a.length > 0){
                a.remove();
            }
            if(!$(el).parent().hasClass("original"))
            {
                var pattern = new RegExp("(" + prefix + "-(\\d+|__prefix__|empty))" + "-id");
                var pattern2 = new RegExp("add_");  //can't be "a", should merge pattern & pattern2
                if(pattern.exec(el.id) && !pattern2.exec(el.id)){
                    var str;                    

                    var obj_id =el.value;
             
                    if('' == obj_id){
                        if("False" == options.isMany2Many && "False" == options.isInitSearch){
                            str = '<a id = "add_' + el.id;
                            str = str + '" class="add-another gifCenter"' ;                    
                            str = str + ' onclick="return showAddAnotherPopup(this);"' ;
                            str = str + ' href="' + options.href_prefix + '/add/' + '"';
                            str = str + ' >';
                            str = str + '<img width="10" height="10" alt="Add Another" src=' + options.bg_addlink + '>';
                        }
                        else{
                            str = '<a id = "lookup_' + el.id;
                            str = str + '" class="add-another gifCenter"' ;                    
                            str = str + ' onclick="return showRelatedObjectLookupPopup(this);"' ;
                            str = str + ' href="' + options.href_prefix + '/?t=id' + '"';
                            str = str + ' >';
                            str = str + '<img width="10" height="10" alt="Add Another" src=' + options.bg_searchlink + '>';                            
                        }
                    }
                    else{
                        str = '<a id = "add_' + el.id;
                        str = str + '" class="add-another gifCenter"' ;                    
                        str = str + ' onclick="return showAddAnotherPopup(this);"' ;
                        str = str + ' href="' + options.href_prefix + '/' + obj_id + '"';
                        str = str + ' >';
                        str = str + '<img width="10" height="10" alt="Add Another" src=' + options.bg_changelink + '>';
                    }
                    str = str + '</a>';
                        
                    $(el).before(str);
                }
            }
        }
//end add
      }
      if (el.name) {
        el.name = el.name.replace(id_regex, replacement);
      }
    };


    
    var totalForms = $("#id_" + options.prefix + "-TOTAL_FORMS").attr("autocomplete", "off");
    var nextIndex = parseInt(totalForms.val(), 10);
    var maxForms = $("#id_" + options.prefix + "-MAX_NUM_FORMS").attr("autocomplete", "off");
    // only show the add button if we are allowed to add more items,
        // note that max_num = None translates to a blank string.
    var showAddButton = maxForms.val() === '' || (maxForms.val()-totalForms.val()) > 0;
    
    $this.each(function(i) {
      $(this).not("." + options.emptyCssClass).addClass(options.formCssClass);
    });
    
    if ($this.length && showAddButton) {
      var addButton;
//modify hebin
//      if ($this.attr("tagName") == "TR") {

      var test = $this.attr("tagName");  //undefined
      var trobj = $this.get(0);
      if (trobj && trobj.tagName == "TR") {        

//end modify        
        // If forms are laid out as table rows, insert the
        // "add" button in a new table row:
        var numCols = this.eq(-1).children().length;
//modify hebin
//        $parent.append('<tr class="' + options.addCssClass + '"><td colspan="' + numCols + '"><a href="javascript:void(0)">' + options.addText + "</a></tr>");

        numCols = trobj.childNodes.length;
        $parent.append('<tr class="' + options.addCssClass + '"><td colspan="' + numCols + '"><a href="javascript:void(0)">' + options.addText + "</a></tr>");

//end modify        
        addButton = $parent.find("tr:last a");
      } else {
        // Otherwise, insert it immediately after the last form:
        $this.filter(":last").after('<div class="' + options.addCssClass + '"><a href="javascript:void(0)">' + options.addText + "</a></div>");
        addButton = $this.filter(":last").next().find("a");
      }

      
/**************************************************************************************************

                   " add another "  function

***************************************************************************************************/

      addButton.click(function(e) {
        e.preventDefault();
        var totalForms = $("#id_" + options.prefix + "-TOTAL_FORMS");
        var template = $("#" + options.prefix + "-empty");
        //create html from template
        var row = template.clone(true);
        row.removeClass(options.emptyCssClass)
          .addClass(options.formCssClass)
          .attr("id", options.prefix + "-" + nextIndex);

        if (row.is("tr")) {
          // If the forms are laid out in table rows, insert
          // the remove button into the last table cell:
          row.children(":last").append('<div><a class="' + options.deleteCssClass +'" href="javascript:void(0)">' + options.deleteText + "</a></div>");
        } else if (row.is("ul") || row.is("ol")) {
          // If they're laid out as an ordered/unordered list,
          // insert an <li> after the last list item:
          row.append('<li><a class="' + options.deleteCssClass +'" href="javascript:void(0)">' + options.deleteText + "</a></li>");
        } else {
          // Otherwise, just insert the remove button as the
          // last child element of the form's container:
          row.children(":first").append('<span><a class="' + options.deleteCssClass + '" href="javascript:void(0)">' + options.deleteText + "</a></span>");
        }
        row.find("*").each(function() {
          updateElementIndex(this, options.prefix, totalForms.val());
        });
        // Insert the new form when it has been fully edited
        row.insertBefore($(template));

//add hebin  #here for add as it can retrieve the actual size

        var set = "div#"+options.prefix+ "-" + nextIndex;
        var sFieldset = set + ">fieldset";
        adjust_fieldset_horizontal(sFieldset);    
//end add        
        // Update number of total forms
        $(totalForms).val(parseInt(totalForms.val(), 10) + 1);
        nextIndex += 1;
        // Hide add button in case we've hit the max, except we want to add infinitely
        if ((maxForms.val() !== '') && (maxForms.val()-totalForms.val()) <= 0) {
          addButton.parent().hide();
        }
        // The delete button of each row triggers a bunch of other things
        row.find("a." + options.deleteCssClass).click(function(e) {
          e.preventDefault();
          // Remove the parent form containing this button:
          var row = $(this).parents("." + options.formCssClass);
          row.remove();
          nextIndex -= 1;
          // If a post-delete callback was provided, call it with the deleted form:
          if (options.removed) {
            options.removed(row);
          }
          // Update the TOTAL_FORMS form count.
          var forms = $("." + options.formCssClass);
          $("#id_" + options.prefix + "-TOTAL_FORMS").val(forms.length);
          // Show add button again once we drop below max
          if ((maxForms.val() === '') || (maxForms.val()-forms.length) > 0) {
            addButton.parent().show();
          }
          // Also, update names and ids for all remaining form controls
          // so they remain in sequence:
          for (var i=0, formCount=forms.length; i<formCount; i++)
          {
            updateElementIndex($(forms).get(i), options.prefix, i);
            $(forms.get(i)).find("*").each(function() {
              updateElementIndex(this, options.prefix, i);
            });
          }
        });
        // If a post-add callback was supplied, call it with the added form:
        if (options.added) {
          options.added(row);
        }
      });
    }

//add hebin
      if(options.isLink == "True"){
          var forms = $("." + "dynamic-" + options.prefix);
          $("#id_" + options.prefix + "-TOTAL_FORMS").val(forms.length);
          for (var i=0, formCount=forms.length; i<formCount; i++)
          {
            updateElementIndex($(forms).get(i), options.prefix, i);
            $(forms.get(i)).find("*").each(function() {
              updateElementIndex(this, options.prefix, i);
            });
          }
      }
//end    
    
    return this;
  };

  /* Setup plugin defaults */
  $.fn.formset.defaults = {
    prefix: "form",          // The form prefix for your django formset
    addText: "add another",      // Text for the add link
    deleteText: "remove",      // Text for the delete link
    addCssClass: "add-row",      // CSS class applied to the add link
    deleteCssClass: "delete-row",  // CSS class applied to the delete link
    emptyCssClass: "empty-row",    // CSS class applied to the empty row
    formCssClass: "dynamic-form",  // CSS class applied to each form in a formset
    added: null,          // Function called each time a new form is added
    removed: null          // Function called each time a form is deleted
  };


  // Tabular inlines ---------------------------------------------------------
  $.fn.tabularFormset = function(options) {  //this = the elem who call tabularFormset function, options = parameter in calling function
    var $rows = $(this);
    var alternatingRows = function(row) {
      $($rows.selector).not(".add-row").removeClass("row1 row2")
        .filter(":even").addClass("row1").end()
        .filter(":odd").addClass("row2");
    };

    var reinitDateTimeShortCuts = function() {
      // Reinitialize the calendar and clock widgets by force
      if (typeof DateTimeShortcuts != "undefined") {
        $(".datetimeshortcuts").remove();
        DateTimeShortcuts.init();
      }
    };

    var updateSelectFilter = function() {
      // If any SelectFilter widgets are a part of the new form,
      // instantiate a new SelectFilter instance for it.
      if (typeof SelectFilter != 'undefined'){
        $('.selectfilter').each(function(index, value){
          var namearr = value.name.split('-');
          SelectFilter.init(value.id, namearr[namearr.length-1], false, options.adminStaticPrefix );
        });
        $('.selectfilterstacked').each(function(index, value){
          var namearr = value.name.split('-');
          SelectFilter.init(value.id, namearr[namearr.length-1], true, options.adminStaticPrefix );
        });
      }
    };

    var initPrepopulatedFields = function(row) {
      row.find('.prepopulated_field').each(function() {
        var field = $(this),
            input = field.find('input, select, textarea'),
            dependency_list = input.data('dependency_list') || [],
            dependencies = [];
        $.each(dependency_list, function(i, field_name) {
          dependencies.push('#' + row.find('.field-' + field_name).find('input, select, textarea').attr('id'));
        });
        if (dependencies.length) {
          input.prepopulate(dependencies, input.attr('maxlength'));
        }
      });
    };

    $rows.formset({
      prefix: options.prefix,
      addText: options.addText,
      formCssClass: "dynamic-" + options.prefix,
      deleteCssClass: "inline-deletelink",
      deleteText: options.deleteText,
      emptyCssClass: "empty-form",
      removed: alternatingRows,
      //add hebin
      bg_addlink : options.bg_addlink,
      bg_changelink : options.bg_changelink,
      bg_searchlink : options.bg_searchlink,      
      isMany2Many: options.isMany2Many,
      isInitSearch: options.isInitSearch,
      href_prefix: options.href_prefix,
      isLink: options.isLink,
      //end add
      added: function(row) {
        initPrepopulatedFields(row);
        reinitDateTimeShortCuts();
        updateSelectFilter();
        alternatingRows(row);
      }
    });

    return $rows;
  };

  // Stacked inlines ---------------------------------------------------------
  $.fn.stackedFormset = function(options) {
    var $rows = $(this);
    var updateInlineLabel = function(row) {
      $($rows.selector).find(".inline_label").each(function(i) {
        var count = i + 1;
        $(this).html($(this).html().replace(/(#\d+)/g, "#" + count));
      });
    };

    var reinitDateTimeShortCuts = function() {
      // Reinitialize the calendar and clock widgets by force, yuck.
      if (typeof DateTimeShortcuts != "undefined") {
        $(".datetimeshortcuts").remove();
        DateTimeShortcuts.init();
      }
    };

    var updateSelectFilter = function() {
      // If any SelectFilter widgets were added, instantiate a new instance.
      if (typeof SelectFilter != "undefined"){
        $(".selectfilter").each(function(index, value){
          var namearr = value.name.split('-');
          SelectFilter.init(value.id, namearr[namearr.length-1], false, options.adminStaticPrefix);
        });
        $(".selectfilterstacked").each(function(index, value){
          var namearr = value.name.split('-');
          SelectFilter.init(value.id, namearr[namearr.length-1], true, options.adminStaticPrefix);
        });
      }
    };

    var initPrepopulatedFields = function(row) {
      row.find('.prepopulated_field').each(function() {
        var field = $(this),
            input = field.find('input, select, textarea'),
            dependency_list = input.data('dependency_list') || [],
            dependencies = [];
        $.each(dependency_list, function(i, field_name) {
          dependencies.push('#' + row.find('.form-row .field-' + field_name).find('input, select, textarea').attr('id'));
        });
        if (dependencies.length) {
          input.prepopulate(dependencies, input.attr('maxlength'));
        }
      });
    };

    $rows.formset({
      prefix: options.prefix,
      addText: options.addText,
      formCssClass: "dynamic-" + options.prefix,
      deleteCssClass: "inline-deletelink",
      deleteText: options.deleteText,
      emptyCssClass: "empty-form",
      removed: updateInlineLabel,
      added: (function(row) {
        initPrepopulatedFields(row);
        reinitDateTimeShortCuts();
        updateSelectFilter();
        updateInlineLabel(row);
      })
    });

    return $rows;
  };
})(django.jQuery);
