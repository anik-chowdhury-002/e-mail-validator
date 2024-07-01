import streamlit as st

def validate_email(email):
    errors = []

    if len(email) < 6:
        errors.append("Email should be at least 6 characters long.")

    if not email[0].isalpha():
        errors.append("The first character should be an alphabet.")

    if email.count("@") != 1:
        errors.append("Email should contain exactly one '@' character.")

    if not ((email[-4] == ".") ^ (email[-3] == ".")):
        errors.append("Email should contain a '.' either at the 3rd or 4th position from the end.")

    if any(c.isspace() for c in email):
        errors.append("Email should not contain any spaces.")

    if any(c.isupper() for c in email):
        errors.append("Email should not contain any capital letters.")

    if any(c not in ("_", ".", "@") and not c.isalnum() for c in email):
        errors.append("Email should not contain special characters other than '_', '.', and '@'.")

    return errors

def main():
    st.title("Email Validator")

    email = st.text_input("Enter your email-Id which you want to check:")

    if st.button("Validate"):
        if email:
            errors = validate_email(email)
            if errors:
                for error in errors:
                    st.error(error)
            else:
                st.success("Valid email")
        else:
            st.warning("Please enter an email-Id")

if __name__ == "__main__":
    main()
