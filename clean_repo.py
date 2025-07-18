import os
import shutil
import subprocess
import sys

def run_command(cmd, cwd=None):
    """Run a command and return the result"""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error running: {cmd}")
            print(f"Error: {result.stderr}")
            return False
        return True
    except Exception as e:
        print(f"Exception running {cmd}: {e}")
        return False

def main():
    print("Creating clean portfolio repository...")
    
    # Get current directory
    current_dir = os.getcwd()
    portfolio_dir = current_dir
    clean_dir = os.path.join(os.path.dirname(current_dir), "portfolio-clean")
    
    # Check if portfolio directory exists
    if not os.path.exists(portfolio_dir):
        print(f"Error: {portfolio_dir} not found!")
        return
    
    # Remove clean directory if it exists
    if os.path.exists(clean_dir):
        shutil.rmtree(clean_dir)
    
    # Create clean directory
    os.makedirs(clean_dir)
    
    # Copy all files except .git folder
    print("Copying files...")
    for item in os.listdir(portfolio_dir):
        if item == '.git':
            continue
        src = os.path.join(portfolio_dir, item)
        dst = os.path.join(clean_dir, item)
        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)
    
    # Initialize git repository
    print("Initializing git repository...")
    if not run_command("git init", clean_dir):
        return
    
    # Set git config
    print("Setting git configuration...")
    if not run_command('git config user.name "Sorbieskis"', clean_dir):
        return
    if not run_command('git config user.email "ds.suchanka@gmail.com"', clean_dir):
        return
    
    # Add all files
    print("Adding files to git...")
    if not run_command("git add -A", clean_dir):
        return
    
    # Commit
    print("Creating initial commit...")
    commit_msg = "Initial commit - Professional portfolio website showcasing engineering case studies"
    if not run_command(f'git commit -m "{commit_msg}"', clean_dir):
        return
    
    print("\n" + "="*50)
    print("SUCCESS! Clean repository created!")
    print("="*50)
    print(f"Location: {clean_dir}")
    print("\nNext steps:")
    print("1. Create new repository on GitHub")
    print("2. cd ../portfolio-clean")
    print("3. git remote add origin https://github.com/Sorbieskis/[REPO_NAME].git")
    print("4. git push -u origin main")
    print("5. Setup GitHub Pages in repository settings")

if __name__ == "__main__":
    main()