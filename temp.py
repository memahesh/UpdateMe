from update_me import UpdateMe

sm = UpdateMe()

sm.setSubject("Update 1")

sm.setInfo("Some Important Info")

sm.addRow("Section 1", "success", "Successfully Completed")

sm.addRow("Section 2", "info", "Some Information")

sm.addRow("Section 3", "danger", "Something went wrong")

sm.showRows()

sm.message_html()

sm.raw_message()

sm.send_update()