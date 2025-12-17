#!/usr/bin/env python3
"""
Quick Deployment Helper for GRA Prototype
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return None

def check_git_status():
    """Check if git is initialized and has commits"""
    if not os.path.exists('.git'):
        print("❌ Git not initialized. Run 'git init' first.")
        return False
    
    result = run_command("git status --porcelain", "Checking git status")
    if result is not None and result.strip():
        print("⚠️  You have uncommitted changes. Commit them first:")
        print("   git add .")
        print("   git commit -m 'Your commit message'")
        return False
    
    return True

def deploy_to_github():
    """Deploy to GitHub"""
    print("\n🐙 GitHub Deployment")
    print("=" * 40)
    
    if not check_git_status():
        return False
    
    print("📋 To deploy to GitHub:")
    print("1. Go to https://github.com/new")
    print("2. Create a repository named 'gra-prototype'")
    print("3. Don't initialize with README")
    print("4. Copy the repository URL")
    print("\nThen run these commands:")
    print("git remote add origin https://github.com/YOUR_USERNAME/gra-prototype.git")
    print("git branch -M main")
    print("git push -u origin main")
    
    return True

def deploy_to_railway():
    """Instructions for Railway deployment"""
    print("\n🚂 Railway Deployment")
    print("=" * 40)
    
    print("📋 Steps to deploy to Railway:")
    print("1. Push your code to GitHub first (see GitHub deployment above)")
    print("2. Go to https://railway.app")
    print("3. Sign up/Login with GitHub")
    print("4. Click 'New Project' → 'Deploy from GitHub repo'")
    print("5. Select your 'gra-prototype' repository")
    print("6. Railway will auto-detect Python and deploy")
    print("7. Your app will be live at: https://your-app.railway.app")
    
    print("\n🔧 Optional: Set environment variables in Railway dashboard:")
    print("   GRA_HOST=0.0.0.0")
    print("   GRA_PORT=$PORT")
    print("   GRA_DEBUG=false")

def deploy_to_render():
    """Instructions for Render deployment"""
    print("\n🎨 Render Deployment")
    print("=" * 40)
    
    print("📋 Steps to deploy to Render:")
    print("1. Push your code to GitHub first")
    print("2. Go to https://render.com")
    print("3. Sign up/Login with GitHub")
    print("4. Click 'New' → 'Web Service'")
    print("5. Connect your GitHub repository")
    print("6. Configure:")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Start Command: python backend/main.py")
    print("   - Environment: Python 3")
    print("7. Click 'Create Web Service'")

def deploy_to_heroku():
    """Instructions for Heroku deployment"""
    print("\n🟣 Heroku Deployment")
    print("=" * 40)
    
    # Check if Heroku CLI is installed
    heroku_check = run_command("heroku --version", "Checking Heroku CLI")
    
    if heroku_check is None:
        print("❌ Heroku CLI not installed.")
        print("📥 Install from: https://devcenter.heroku.com/articles/heroku-cli")
        return False
    
    print("📋 Heroku deployment commands:")
    print("heroku login")
    print("heroku create your-gra-prototype")
    print("git push heroku main")
    print("heroku open")
    
    # Create Procfile if it doesn't exist
    if not os.path.exists('Procfile'):
        with open('Procfile', 'w') as f:
            f.write('web: python backend/main.py\n')
        print("✅ Created Procfile")

def deploy_docker():
    """Instructions for Docker deployment"""
    print("\n🐳 Docker Deployment")
    print("=" * 40)
    
    # Check if Docker is installed
    docker_check = run_command("docker --version", "Checking Docker")
    
    if docker_check is None:
        print("❌ Docker not installed.")
        print("📥 Install from: https://docker.com/get-started")
        return False
    
    print("📋 Docker deployment commands:")
    print("# Build the image")
    print("docker build -t gra-prototype .")
    print("\n# Run locally")
    print("docker run -p 8000:8000 gra-prototype")
    print("\n# Or use docker-compose")
    print("docker-compose up -d")

def show_deployment_options():
    """Show all deployment options"""
    print("🚀 GRA Prototype Deployment Options")
    print("=" * 50)
    
    options = {
        "1": ("GitHub (Version Control)", deploy_to_github),
        "2": ("Railway (Recommended)", deploy_to_railway),
        "3": ("Render (Free Tier)", deploy_to_render),
        "4": ("Heroku (Classic)", deploy_to_heroku),
        "5": ("Docker (Any Cloud)", deploy_docker),
        "6": ("Show All Options", lambda: None)
    }
    
    print("\nChoose your deployment platform:")
    for key, (name, _) in options.items():
        print(f"   {key}. {name}")
    
    choice = input("\nEnter your choice (1-6): ").strip()
    
    if choice in options:
        name, func = options[choice]
        if func:
            func()
        else:
            # Show all options
            for _, (_, f) in options.items():
                if f:
                    f()
    else:
        print("❌ Invalid choice")

def main():
    """Main deployment helper"""
    print("🎯 GRA Prototype Deployment Helper")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('backend/main.py'):
        print("❌ Please run this script from the gra-prototype directory")
        sys.exit(1)
    
    # Check if tests have been run
    if not os.path.exists('FINAL_TEST_REPORT.md'):
        print("⚠️  No test report found. Run tests first:")
        print("   python test_system.py")
        print("")
    
    show_deployment_options()
    
    print("\n" + "=" * 50)
    print("🎉 Deployment Guide Complete!")
    print("\n💡 Quick Recommendations:")
    print("   🥇 For beginners: GitHub → Railway")
    print("   🥈 For free hosting: GitHub → Render")
    print("   🥉 For enterprise: GitHub → Docker → AWS/GCP")
    
    print("\n📚 For detailed instructions, see:")
    print("   - DEPLOYMENT_GUIDE.md")
    print("   - README.md")

if __name__ == "__main__":
    main()