import os
#latest_version = "${{ env.LATEST_VERSION }}".strip('v')
latest_version='0.1.0'
#print(os.getenv('GITHUB_ENV'))

lines = list()
dev_header_detected = False
with open("CHANGELOG.md", "r") as infile:
    for line in infile:
        if latest_version in line:
            break
        elif line.startswith('#') and 'dev' in line:
           dev_header_detected = True
        elif dev_header_detected:
          lines.append(line)
release_notes = ''.join(lines)
print(release_notes)
#with open(os.getenv("GITHUB_ENV"), "a") as env_file:
#    env_file.write(f"RELEASE_NOTES='f{release_notes}'")
