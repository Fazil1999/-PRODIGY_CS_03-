def check_password_strength(password):
  """Evaluates password strength based on various criteria.

  Args:
      password: The password to be checked.

  Returns:
      A tuple containing:
          - strength_score (int): Numerical score representing strength (higher is better).
          - feedback (str): Descriptive feedback about password strength.
  """
  score = 0
  feedback = ""

  # Check password length
  if len(password) >= 12:
    score += 2
    feedback += "Length is strong (12+ characters).\n"
  elif len(password) >= 8:
    score += 1
    feedback += "Length is good (8-11 characters).\n"
  else:
    feedback += "Length is weak (less than 8 characters). Consider using a longer password.\n"

  # Check for uppercase letters
  if any(char.isupper() for char in password):
    score += 1
    feedback += "Contains uppercase letters.\n"
  else:
    feedback += "Consider adding uppercase letters for increased security.\n"

  # Check for lowercase letters
  if any(char.islower() for char in password):
    score += 1
    feedback += "Contains lowercase letters.\n"
  else:
    feedback += "Consider adding lowercase letters for increased security.\n"

  # Check for numbers
  if any(char.isdigit() for char in password):
    score += 1
    feedback += "Contains numbers.\n"
  else:
    feedback += "Consider adding numbers for increased security.\n"

  # Check for special characters
  if any(char in "!@#$%^&*()-=_+[]{};:'\",<.>/? " for char in password):
    score += 1
    feedback += "Contains special characters.\n"
  else:
    feedback += "Consider adding special characters for increased security.\n"

  # Determine overall strength based on score
  strength = "Very Weak"
  if score >= 4:
    strength = "Strong"
  elif score >= 3:
    strength = "Good"
  elif score >= 2:
    strength = "Moderate"

  return score, f"Password Strength: {strength}\n{feedback}"

def main():
  """Prompts user for password and displays strength assessment."""
  password = input("Enter your password: ")
  score, feedback = check_password_strength(password)
  print(feedback)

if __name__ == "__main__":
  main()
