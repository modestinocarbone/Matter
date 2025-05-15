# Name of the Python source file
SCRIPT_NAME = for_matter.py
# Command name you want to use (without .py)
CMD_NAME = matter
# Installation path (can be modified)
INSTALL_PATH = $(HOME)/.local/bin

# Adds the shebang if not present
fix-shebang:
	@if ! grep -q '^#!.*python' $(SCRIPT_NAME); then \
		echo "Adding shebang to $(SCRIPT_NAME)"; \
		echo '#!/usr/bin/env python3\n' | cat - $(SCRIPT_NAME) > temp && mv temp $(SCRIPT_NAME); \
	fi

# Makes the file executable
make-executable:
	chmod +x $(SCRIPT_NAME)

# Creates the directory if it doesn't exist and copies the script as a command
install: fix-shebang make-executable
	mkdir -p $(INSTALL_PATH)
	cp $(SCRIPT_NAME) $(INSTALL_PATH)/$(CMD_NAME)
	echo "Installed as $(CMD_NAME) in $(INSTALL_PATH)"

# Removes the installed file
uninstall:
	rm -f $(INSTALL_PATH)/$(CMD_NAME)
	echo "Removed $(CMD_NAME) from $(INSTALL_PATH)"

# Generic cleanup (you can add more here)
clean:
	rm -f temp
