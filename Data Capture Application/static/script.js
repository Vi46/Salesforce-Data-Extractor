function tableClick() {
    var div1 = document.getElementById("div1");
    var div2 = document.getElementById("div2");

    var computedStyleDiv1 = window.getComputedStyle(div1).getPropertyValue('display');

    if (computedStyleDiv1 === "block") {
        console.log('tableClick');
        div1.style.display = "none";
        div2.style.display = "block";
    }
}

function gridClick() {
    var div1 = document.getElementById("div1");
    var div2 = document.getElementById("div2");

    var computedStyleDiv2 = window.getComputedStyle(div2).getPropertyValue('display');

    console.log('gridClick');
    if (computedStyleDiv2 === "block") {
        console.log('gridClick');
        div1.style.display = "block";
        div2.style.display = "none";
    }
}

function exportCSV() {
    let csvContent = "data:text/csv;charset=utf-8,";
    csvContent += "Type,Count\n";
    
    const counts = {
      'Apex Class Count': apex_class_count,
      'Flow Count': flow_count,
      'Apex Trigger Count': apex_trigger_count,
      'Lightning Component Count': lightning_component_count,
      'Custom Object Count': custom_object_count,
      'Custom Permission Set Count': custom_permission_set_count,
      'Custom Labels Count': custom_labels_count,
      'Custom Tab Count': custom_tab_count,
      'Role Count': role_count,
      'Global Value Set Count': global_value_set_count,
      'Custom Application Count': Custom_Application_count,
      'Custom Notification Type Count': Custom_Notification_Type_count,
      'Page Layout Count': page_layout_count,
      'Profile Count': Profile_count,
      'WorkFlow FieldUpdate Count': WorkFlow_FieldUpdate_count,
      'WorkFlow Alert Count': workFlow_alert_count,
      'Content Asset Count': ContentAsset_count,
      'Flexipage Count': flexipage_count,
      'Duplicate Rule Count': DuplicateRule_count,
      'Email Template Count': EmailTemplate_count,
      'Process Definition Count': ProcessDefinition_count,
      'Group Count': Group_count,
      'Static Resource Count': StaticResource_count,
    };

    // Iterate over counts and add them to the CSV content
    for (const [type, count] of Object.entries(counts)) {
      csvContent += "${type},${count}\n";
    }

    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "export.csv");
    document.body.appendChild(link);

    link.click();
  }