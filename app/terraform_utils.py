import os
import subprocess

def write_terraform_code(terraform_code):
    """Write the Terraform code to a .tf file."""
    with open("generated/main.tf", "w") as file:
        file.write(terraform_code)

def deploy_terraform():
    """Run Terraform commands to deploy the infrastructure."""
    try:
        # Initialize Terraform
        subprocess.run(["terraform", "init"], cwd="generated", check=True)
        
        # Apply Terraform (auto-approve for automation)
        subprocess.run(["terraform", "apply", "-auto-approve"], cwd="generated", check=True)
        return "Terraform applied successfully."
    except subprocess.CalledProcessError as e:
        return f"Terraform deployment failed: {e}"
