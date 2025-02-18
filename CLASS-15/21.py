def send_email(default='en'):

    if default =='en':
        email_body = """
        Dear {name},

        We are excited to invite you to the {event} on {date}.

        Location: {location}

        Hoping to see you there!
        """

        return email_body.format(
            name="nahid", event = "Reunion",
            date = "10-10-24", location = "Motijheel"
        )
    
    elif default =='bn':
        email_body = """




    """

print(send_email())