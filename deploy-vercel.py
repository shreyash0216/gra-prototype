#!/usr/bin/env python3
"""
Vercel Deployment Helper for GRA Prototype
"""

import os
import subprocess
import sys

def check_vercel_cli():
    """Check if Vercel CLI is installed"""
    try:
        result = subprocess.run(['vercel', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Vercel CLI installed: {result.stdout.strip()}")
            return True
        else:
            return False
    except FileNotFoundError:
        return False

def install_vercel_cli():
    """Instructions to install Vercel CLI"""
    print("❌ Vercel CLI not found")
    print("\n📥 Install Vercel CLI:")
    print("   npm install -g vercel")
    print("   # or")
    print("   yarn global add vercel")
    print("\n💡 Don't have Node.js? Download from: https://nodejs.org")
    return False

def deploy_to_vercel():
    """Deploy to Vercel"""
    print("🚀 Deploying to Vercel...")
    print("=" * 40)
    
    if not check_vercel_cli():
        return install_vercel_cli()
    
    print("\n📋 Vercel Deployment Steps:")
    print("1. Login to Vercel")
    print("2. Deploy the project")
    print("3. Get your live URL")
    
    # Login
    print("\n🔐 Step 1: Login to Vercel")
    try:
        subprocess.run(['vercel', 'login'], check=True)
        print("✅ Logged in to Vercel")
    except subprocess.CalledProcessError:
        print("❌ Login failed")
        return False
    
    # Deploy
    print("\n🚀 Step 2: Deploying...")
    try:
        result = subprocess.run(['vercel', '--prod'], capture_output=True, text=True, check=True)
        print("✅ Deployment successful!")
        
        # Extract URL from output
        output_lines = result.stdout.split('\n')
        for line in output_lines:
            if 'https://' in line and 'vercel.app' in line:
                url = line.strip()
                print(f"\n🌐 Your GRA Prototype is live at:")
                print(f"   {url}")
                print(f"\n📚 API Documentation:")
                print(f"   {url}/api/docs")
                return url
        
        print("✅ Deployed successfully, but couldn't extract URL")
        print("Check your Vercel dashboard for the URL")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Deployment failed: {e}")
        print("\n💡 Common issues:")
        print("   • Make sure you're in the project directory")
        print("   • Check vercel.json configuration")
        print("   • Verify all files are committed to git")
        return False
    
    return True

def manual_vercel_steps():
    """Show manual Vercel deployment steps"""
    print("📋 Manual Vercel Deployment Steps")
    print("=" * 40)
    
    print("\n🌐 Option 1: Vercel Dashboard (Easiest)")
    print("1. Go to https://vercel.com")
    print("2. Sign up/Login with GitHub")
    print("3. Click 'New Project'")
    print("4. Import your 'gra-prototype' repository")
    print("5. Vercel auto-detects settings")
    print("6. Click 'Deploy'")
    print("7. Get your live URL!")
    
    print("\n💻 Option 2: Vercel CLI")
    print("1. Install: npm install -g vercel")
    print("2. Login: vercel login")
    print("3. Deploy: vercel --prod")
    print("4. Follow prompts")
    
    print("\n⚙️ Project Settings (if needed):")
    print("   • Framework Preset: Other")
    print("   • Build Command: (leave empty)")
    print("   • Output Directory: frontend")
    print("   • Install Command: pip install -r requirements-vercel.txt")

def test_vercel_deployment():
    """Test Vercel deployment"""
    print("\n🧪 Test Your Vercel Deployment")
    print("-" * 30)
    
    url = input("Enter your Vercel URL: ").strip()
    if not url:
        return
    
    if not url.startswith('http'):
        url = 'https://' + url
    
    url = url.rstrip('/')
    
    print(f"\n🔍 Testing: {url}")
    
    try:
        import requests
        
        # Test API
        response = requests.get(f"{url}/api", timeout=10)
        if response.status_code == 200:
            print("✅ API is working!")
            
            # Test query
            test_query = {"query": "What is RAG?", "context": "Testing"}
            response = requests.post(f"{url}/api/query", json=test_query, timeout=15)
            if response.status_code == 200:
                print("✅ Query processing works!")
            
            # Test simulation
            sim_request = {"scenario_type": "basic_query", "parameters": {"query_count": 3}}
            response = requests.post(f"{url}/api/simulate", json=sim_request, timeout=15)
            if response.status_code == 200:
                print("✅ Simulation works!")
            
            print(f"\n🎉 Your GRA Prototype is fully functional!")
            print(f"🌐 Live URL: {url}")
            print(f"📱 Frontend: {url}")
            print(f"🔧 API: {url}/api")
            
        else:
            print(f"❌ API not responding: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Test failed: {e}")

def main():
    """Main deployment function"""
    print("🎯 Vercel Deployment for GRA Prototype")
    print("=" * 50)
    
    print("\n🎯 Choose deployment method:")
    print("1. Auto-deploy with Vercel CLI")
    print("2. Manual deployment instructions")
    print("3. Test existing Vercel deployment")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == "1":
        deploy_to_vercel()
    elif choice == "2":
        manual_vercel_steps()
    elif choice == "3":
        test_vercel_deployment()
    else:
        print("Invalid choice")
        manual_vercel_steps()
    
    print("\n💡 Vercel Benefits:")
    print("   ✅ Free tier with generous limits")
    print("   ✅ Automatic HTTPS")
    print("   ✅ Global CDN")
    print("   ✅ Automatic deployments from GitHub")
    print("   ✅ Serverless functions")

if __name__ == "__main__":
    main()