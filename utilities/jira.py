# from jira import JIRA
# from settings.config import script_settings
# import logging
#
# jira = None
# issue = ""
# execution_status = ""
#
#
# def connect_to_jira():
#     jira_server = {'server': script_settings['jira_server']}
#     global jira
#     jira = JIRA(options=jira_server, basic_auth=(script_settings['jira_user'], script_settings['jira_token']))
#     if jira is not None:
#         logging.info('Successfully connected to Jira')
#
#
# def get_issue_by_key(issue_key):
#     # global issue
#     # issue = jira.issue(issue_key)
#     return jira.issue(issue_key)
#
#
# def get_execution_status(status):
#     global execution_status
#     execution_status = status
#
#
# def add_issue(summary, description):
#     return jira.create_issue(project=script_settings['jira_project_key'], summary=summary, description=description,
#                              issuetype={'name': 'Bug'})
#
#
# def transition_issue():
#     jira.transition_issue(issue, transition='Ready For Test')
#     jira.transition_issue(issue, transition='Test in Progress')
#     jira.transition_issue(issue, transition=execution_status)
#
#
# def attach_screenshots_in_jira(issue_to_attach, attachment_path):
#     # for attachment in issue.fields.attachment:
#     #     jira.delete_attachment(attachment['id'])
#     jira.add_attachment(issue=issue_to_attach, attachment=attachment_path)
#
#
# def add_comment():
#     list_of_comments = jira.comments(issue)
#     # if len(list_of_comments) > 0:
#     #     for comment in list_of_comments:
#     #         comment.delete()
#     jira.add_comment(issue,
#                      'Automated Test Execution Reports available at Azure pipelines')
#
#
# def update_description(field_name):
#     issue.update(description=field_name)
#
#
# def add_issues_to_epic(epic, issue_to_add):
#     jira.add_issues_to_epic(epic, issue_to_add)
#
#
# def update_label(issue_to_update):
#     label = script_settings['jira_label']
#     issue_to_update.update(fields={"labels": [label]})
