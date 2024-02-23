from flask import Flask, Response, render_template,request, stream_with_context
from simple_salesforce import Salesforce
import requests


app = Flask(__name__)



# Salesforce API credentials
username = 'vishaldev@cct.com'
password = 'Pluto#21'
security_token = 'sSk5ZBgYkTdTPSdTer9ZiHky'
api_version = 'v57.0'

login_url = 'https://login.salesforce.com'
tooling_api_endpoint = f'https://cloudchamptechnologies16-dev-ed.my.salesforce.com/services/data/{api_version}/tooling/query'

payload = {
    'grant_type': 'password',
    'client_id': '3MVG9wt4IL4O5wvKWCHOWdmDDMQZcUh18IfDSt5w2u4QqgJEHMQ2UGabXj5ZQ5Oj7T4KFhYJ4Lny1NStxGFwT',
    'client_secret': '753278BB635DEB1A69B7D67894AFC5F3DFA091330562C3A1F13F23FDDEF905F5',
    'username': username,
    'password': f'{password}{security_token}'
}

# Get access token
response = requests.post(f'{login_url}/services/oauth2/token', data=payload)
access_token = response.json()['access_token']


# Query for flexipage
flexipage_query = "SELECT Id, DeveloperName From flexipage"
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
response = requests.get(tooling_api_endpoint, headers=headers, params={'q': flexipage_query})
flexipages = response.json()['records']

# Extract count and print information about flexipage
flexipage_count = len(flexipages)
print(f'flexipage count: {flexipage_count}')
for flexipage in flexipages:
    print(f'Id: {flexipage["Id"]}, flexipage: {flexipage["DeveloperName"]}')

# Query for workFlow_alert
workFlow_alert_query = "SELECT Id, DeveloperName From workFlowalert"
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
response = requests.get(tooling_api_endpoint, headers=headers, params={'q': workFlow_alert_query})
workFlow_alerts = response.json()['records']

# Extract count and print information about workFlow_alert
workFlow_alert_count = len(workFlow_alerts)
print(f'WorkFlow FieldUpdate count: {workFlow_alert_count}')
for workFlowalert in workFlow_alerts:
    print(f'Id: {workFlowalert["Id"]}, Page Layout: {workFlowalert["DeveloperName"]}')

# Query for WorkFlowFieldUpdate
WorkFlow_FieldUpdate_query = "SELECT Id,Name FROM workflowfieldupdate"
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
response = requests.get(tooling_api_endpoint, headers=headers, params={'q': WorkFlow_FieldUpdate_query})
WorkFlow_FieldUpdates = response.json()['records']

# Extract count and print information about WorkFlowFieldUpdate
WorkFlow_FieldUpdate_count = len(WorkFlow_FieldUpdates)
print(f'WorkFlow FieldUpdate count: {WorkFlow_FieldUpdate_count}')
for WorkFlow_FieldUpdate in WorkFlow_FieldUpdates:
    print(f'Id: {WorkFlow_FieldUpdate["Id"]}, Page Layout: {WorkFlow_FieldUpdate["Name"]}')

# Query for Page Layout
page_layout_query = "SELECT Id,Name FROM Layout"
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
response = requests.get(tooling_api_endpoint, headers=headers, params={'q': page_layout_query})
page_layouts = response.json()['records']

# Extract count and print information about Page Layout
page_layout_count = len(page_layouts)
print(f'page layout count: {page_layout_count}')
for page_layout in page_layouts:
    print(f'Id: {page_layout["Id"]}, Page Layout: {page_layout["Name"]}')

# Query for Custom Application
Custom_Application_query = "SELECT Id,DeveloperName FROM CustomApplication"
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
response = requests.get(tooling_api_endpoint, headers=headers, params={'q': Custom_Application_query})
Custom_Applications = response.json()['records']

# Extract count and print information about Custom Application 
Custom_Application_count = len(Custom_Applications)
print(f'Global Value Set Count: {Custom_Application_count}')
for Custom_Application in Custom_Applications:
    print(f'Id: {Custom_Application["Id"]}, DeveloperName: {Custom_Application["DeveloperName"]}')

# Query for Global Value Set
global_value_set_query = "SELECT Id,DeveloperName FROM GlobalValueSet"
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
response = requests.get(tooling_api_endpoint, headers=headers, params={'q': global_value_set_query})
global_value_sets = response.json()['records']

# Extract count and print information about Global Value Set
global_value_set_count = len(global_value_sets)
print(f'Global Value Set Count: {global_value_set_count}')
for global_value_set in global_value_sets:
    print(f'Id: {global_value_set["Id"]}, DeveloperName: {global_value_set["DeveloperName"]}')

# Query for Custom tab
custom_tab_query = "SELECT Id,DeveloperName FROM Customtab"
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
response = requests.get(tooling_api_endpoint, headers=headers, params={'q': custom_tab_query})
custom_tabs = response.json()['records']

# Extract count and print information about Custom tab 
custom_tab_count = len(custom_tabs)
print(f'Lightning Component Bundle Count: {custom_tab_count}')
for customtab in custom_tabs:
    print(f'Id: {customtab["Id"]}, DeveloperName: {customtab["DeveloperName"]}')

# Query for Custom Label
query = "SELECT Id,Name FROM CustomLabel"
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
response = requests.get(tooling_api_endpoint, headers=headers, params={'q': query})
custom_labels = response.json()['records']

# Extract count and print information about Custom Label 
custom_labels_count = len(custom_labels)
print(f'Custom Labels Count: {custom_labels_count}')
for customlabel in custom_labels:
    print(f'Id: {customlabel["Id"]}, Name: {customlabel["Name"]}')


# Query for Lightning Component Bundles
query = "SELECT Id, DeveloperName, NamespacePrefix, ApiVersion FROM LightningComponentBundle"
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
response = requests.get(tooling_api_endpoint, headers=headers, params={'q': query})
lightning_component_bundles = response.json()['records']

# Extract count and print information about Lightning Component Bundles
lightning_component_count = len(lightning_component_bundles)
print(f'Lightning Component Bundle Count: {lightning_component_count}')
for bundle in lightning_component_bundles:
    print(f'Id: {bundle["Id"]}, DeveloperName: {bundle["DeveloperName"]}, NamespacePrefix: {bundle.get("NamespacePrefix")}, ApiVersion: {bundle["ApiVersion"]}')

# Create a Salesforce connection
sf = Salesforce(username=username, password=password, security_token=security_token)

# Query for Apex classes
apex_class_query = "SELECT Id, Name, Body FROM ApexClass"
apex_class_result = sf.query(apex_class_query)
apex_classes = apex_class_result['records']
apex_class_count = apex_class_result['totalSize']

# Query for Flows
apex_trigger_query = "SELECT Id, Name FROM ApexTrigger"
apex_trigger_result = sf.query(apex_trigger_query)
triggers = apex_trigger_result['records']
apex_trigger_count = apex_trigger_result['totalSize']

# Query for Flows
flow_query = "SELECT Id, Label FROM FlowDefinitionView"
flow_result = sf.query(flow_query)
flows = flow_result['records']
flow_count = flow_result['totalSize']

# Query for Custom object
custom_object_query = "SELECT Id, QualifiedApiName, Label, DurableId FROM EntityDefinition WHERE DurableId LIKE '01I%'"
custom_object_result = sf.query(custom_object_query)
custom_objects = custom_object_result['records']
custom_object_count = custom_object_result['totalSize']

# Query for custom permission sets
custom_permission_set_query = "SELECT Id, Name, Label FROM PermissionSet WHERE IsCustom = true"
custom_permission_set_result = sf.query(custom_permission_set_query)
custom_permission_sets = custom_object_result['records']
custom_permission_set_count = custom_permission_set_result['totalSize']

# Query for role 
role_query = "SELECT Id, Name, DeveloperName FROM UserRole"
role_result = sf.query(role_query)
roles = role_result['records']
role_count = role_result['totalSize']

# Query for CustomNotificationType
Custom_Notification_Type_query = "SELECT Id,DeveloperName FROM CustomNotificationType"
Custom_Notification_Type_result = sf.query(Custom_Notification_Type_query)
Custom_Notification_Types = Custom_Notification_Type_result['records']
Custom_Notification_Type_count = Custom_Notification_Type_result['totalSize']

# Query for Profile
Profile_query = "SELECT Id,Name FROM Profile"
Profile_result = sf.query(Profile_query)
Profiles = Profile_result['records']
Profile_count = Profile_result['totalSize']

# Query for ContentAsset
ContentAsset_query = "SELECT Id, MasterLabel, NamespacePrefix, DeveloperName FROM ContentAsset"
ContentAsset_result = sf.query(ContentAsset_query)
ContentAssets = ContentAsset_result['records']
ContentAsset_count = ContentAsset_result['totalSize']

# Query for MatchingRule
MatchingRule_query = "SELECT Id, DeveloperName, MasterLabel FROM MatchingRule"
MatchingRule_result = sf.query(MatchingRule_query)
MatchingRules = MatchingRule_result['records']
MatchingRule_count = MatchingRule_result['totalSize']

# Query for DuplicateRule
DuplicateRule_query = "SELECT Id, DeveloperName, MasterLabel FROM DuplicateRule"
DuplicateRule_result = sf.query(DuplicateRule_query)
DuplicateRules = DuplicateRule_result['records']
DuplicateRule_count = DuplicateRule_result['totalSize']

# Query for EmailTemplate
EmailTemplate_query = "SELECT Id, DeveloperName FROM EmailTemplate"
EmailTemplate_result = sf.query(EmailTemplate_query)
EmailTemplates = EmailTemplate_result['records']
EmailTemplate_count = EmailTemplate_result['totalSize']

# Query for ProcessDefinition
ProcessDefinition_query = "SELECT Id, Name, DeveloperName FROM ProcessDefinition"
ProcessDefinition_result = sf.query(ProcessDefinition_query)
ProcessDefinitions = ProcessDefinition_result['records']
ProcessDefinition_count = ProcessDefinition_result['totalSize']

# Query for Queue
Group_query = "SELECT Id, Name, Type FROM Group where type = 'group'"
Group_result = sf.query(Group_query)
Groups = Group_result['records']
Group_count = Group_result['totalSize']

# Query for StaticResource 
StaticResource_query = "SELECT Id, Name FROM StaticResource"
StaticResource_result = sf.query(StaticResource_query)
StaticResources = StaticResource_result['records']
StaticResource_count = StaticResource_result['totalSize']

# Print information about Apex classes, triggers, and flows
print(f'Apex Class Count: {apex_class_count}')
apex_class_dict = {}
for apex_class in apex_classes:
    class_name = apex_class["Id"]
    class_body = apex_class["Body"]
    apex_class_dict[class_name] = class_body

# print(apex_class_dict)

print(f'Flow Count: {flow_count}')
for flow in flows:
    print(f'Flow Label: {flow["Label"]}, Id: {flow["Id"]}')

print(f'Apex Trigger Count: {apex_trigger_count}')
for trigger in triggers:
    print(f'Apex Trigger: {trigger["Name"]}, Id: {trigger["Id"]}')

print(f'object count: {custom_object_count}')
for custom_object in custom_objects:
    print(f'Custom Object: {custom_object["Label"]}, Id: {custom_object["DurableId"]}')

print(f'Custom Permission Set Count: {custom_permission_set_count}')
for custom_permission_set in custom_permission_sets:
    print(f'custom_permission_set: {custom_permission_set["Label"]}, Id: {custom_permission_set["Id"]}')

print(f'role_count: {role_count}')
for role in roles:
    print(f'Role: {role["Name"]}, Id: {role["Id"]}')

print(f'Custom_Notification_Type_count: {Custom_Notification_Type_count}')
for Custom_Notification_Type in Custom_Notification_Types:
    print(f'Custom_Notification_Type: {Custom_Notification_Type["Name"]}, Id: {Custom_Notification_Type["Id"]}')

print(f'Profile Count: {Profile_count}')
for profile in Profiles:
    print(f'profile: {profile["Name"]}, Id: {profile["Id"]}')

print(f'Content Asset Count: {ContentAsset_count}')
for contentAsset in ContentAssets:
    print(f'ContentAsset: {contentAsset["DeveloperName"]}, Id: {contentAsset["Id"]}')

print(f'MatchingRule Count: {MatchingRule_count}')
for MatchingRule in MatchingRules:
    print(f'MatchingRule: {MatchingRule["DeveloperName"]}, Id: {MatchingRule["Id"]}')

print(f'DuplicateRule Count: {DuplicateRule_count}')
for DuplicateRule in DuplicateRules:
    print(f'DuplicateRule: {DuplicateRule["MasterLabel"]}, Id: {DuplicateRule["Id"]}')

print(f'EmailTemplate Count: {EmailTemplate_count}')
for EmailTemplate in EmailTemplates:
    print(f'EmailTemplate: {EmailTemplate["DeveloperName"]}, Id: {EmailTemplate["Id"]}')

print(f'ProcessDefinition Count: {ProcessDefinition_count}')
for ProcessDefinition in ProcessDefinitions:
    print(f'ProcessDefinition: {ProcessDefinition["DeveloperName"]}, Id: {ProcessDefinition["Id"]}')

print(f'Group Count: {Group_count}')
for Group in Groups:
    print(f'Group: {Group["DeveloperName"]}, Id: {Group["Id"]}')

print(f'StaticResource Count: {StaticResource_count}')
for StaticResource in StaticResources:
    print(f'StaticResource: {StaticResource["DeveloperName"]}, Id: {StaticResource["Id"]}')

# Define a route to render the HTML template
@app.route('/')
def index():
    return render_template('new.html', apex_class_count=apex_class_count,
                           apex_class_dict=apex_class_dict,
                           flow_count=flow_count, flows=flows,
                           apex_trigger_count=apex_trigger_count, triggers=triggers,
                           lightning_component_count=lightning_component_count,
                           custom_object_count=custom_object_count,
                           custom_permission_set_count=custom_permission_set_count,
                           custom_labels_count=custom_labels_count,
                           custom_tab_count=custom_tab_count,
                           role_count=role_count,
                           global_value_set_count=global_value_set_count,
                           Custom_Application_count=Custom_Application_count,
                           Custom_Notification_Type_count=Custom_Notification_Type_count,
                           page_layout_count=page_layout_count,
                           Profile_count=Profile_count,
                           WorkFlow_FieldUpdate_count=WorkFlow_FieldUpdate_count,
                           workFlow_alert_count=workFlow_alert_count,
                           ContentAsset_count=ContentAsset_count,
                           flexipage_count=flexipage_count,
                           DuplicateRule_count=DuplicateRule_count,
                           EmailTemplate_count=EmailTemplate_count,
                           ProcessDefinition_count=ProcessDefinition_count,
                           Group_count=Group_count,
                           StaticResource_count=StaticResource_count,
                           username=username)


@app.route('/download_csv')
def download_csv():
    # Get count values from your data
    counts_data = {
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
    }

    # Define CSV response
    csv_data = generate_csv(counts_data)

    # Create a CSV response
    response = Response(stream_with_context(csv_data))
    response.headers['Content-Type'] = 'text/csv'
    response.headers['Content-Disposition'] = 'attachment; filename=counts_data.csv'

    return response

def generate_csv(data):
    # Function to generate CSV data from the counts_data dictionary
    yield ','.join(['Count Name', 'Count Value']) + '\n'
    for count_name, count_value in data.items():
        yield f'{count_name},{count_value}\n'
        
@app.route('/submit', methods=['POST'])
def submit():
    global re_username, re_password, re_security_token, re_client_id, re_client_secret
    # rest of your submit function
    print(request.form)  # Print the entire form data
    re_username = request.form.get('username')
    re_password = request.form.get('password')
    re_security_token = request.form.get('security_token')
    re_client_id = request.form.get('client_id')
    re_client_secret = request.form.get('client_secret')

    # Do something with the form data (e.g., print it)
    print(f"Username: {re_username}")
    print(f"Password: {re_password}")
    print(f"Security Token: {re_security_token}")
    print(f"Client ID: {re_client_id}")
    print(f"Client Secret: {re_client_secret}")

    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)


