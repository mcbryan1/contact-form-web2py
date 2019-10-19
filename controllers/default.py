def contact():
    return dict()
    
def store():
    submitted_name = request.vars.name
    submitted_email = request.vars.email
    submitted_phone = request.vars.phone
    submitted_message = request.vars.message

    results = db.users.insert(
        db_name = submitted_name,
        db_email = submitted_email,
        db_phone = submitted_phone,
        db_message = submitted_message
    )

    if results:
        return "Message Successfully Sent"
    else:
        return "An Error Occured"