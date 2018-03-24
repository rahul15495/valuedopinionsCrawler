import subprocess

total_forms= 17

for i in range(total_forms):
	subprocess.call(["python", "signup_survey_parts.py"])