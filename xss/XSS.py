def display_comment(comment):
  """Displays the given comment on the web page."""
  print(comment)


# Without output encoding:
user_comment = input("Enter a comment: ")


# Display the comment without encoding it.
display_comment(user_comment)


# With output encoding:
user_comment = input("Enter a comment: ")


# Encode the comment before displaying it.
encoded_comment = html.escape(user_comment)


display_comment(encoded_comment)