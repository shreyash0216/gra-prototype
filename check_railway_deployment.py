#!/usr/bin/env python3
"""
Check Railway deployment status and find URL
"""

import requests
import time
import sys

def check_railway_deployment():
    """Guide user through checking Railway deployment"""
    print("🚂 Railway Deployment Checker")
    print("=" * 50)
    
    print("\n📋 Step-by-Step Railway URL Finding:")
    print("1. Go to https://railway.app/dashboard")
    print("2. Click on your 'gra-prototype' project")
    print("3. You should see your deployment status")
    
    print("\n🔍 Where to find your URL:")
    print("📍 Method 1 - Project Overview:")
    print("   • Look for a 'Deployments' section")
    print("   • Find 'Public URL' or 'Domain'")
    print("   • Copy the URL (ends with .railway.app)")
    
    print("\n📍 Method 2 - Settings Tab:")
    print("   • Click 'Settings' tab")
    print("   • Look for 'Networking' or 'Domains'")
    print("   • Find your public domain")
    
    print("\n📍 Method 3 - Deployment Logs:")
    print("   • Click 'Deployments' tab")
    print("   • Click on latest deployment")
    print("   • Look for 'Your app is live at: https://...'")
    
    print("\n🚨 If deployment is failing:")
    print("   • Check the logs in Railway dashboard")
    print("   • Look for error messages")
    print("   • Common issues:")
    print("     - Port binding (should be fixed now)")
    print("     - Memory limits")
    print("     - Build failures")
    
    print("\n⏱️  Deployment Status Check:")
    print("   • 🟢 Running = Your app is live")
    print("   • 🟡 Building = Wait a few minutes")
    print("   • 🔴 Failed = Check logs for errors")
    
    # Try to help find URL
    print("\n🔍 Let me try to find your URL...")
    print("Enter your Railway project URL (the one you shared earlier):")
    project_url = input("Project URL: ").strip()
    
    if "railway.com/project/" in project_url:
        # Extract project ID
        try:
            project_id = project_url.split("/project/")[1].split("/")[0]
            print(f"\n📋 Project ID: {project_id}")
            
            # Try common patterns
            patterns = [
                f"https://web-production-{project_id[:4]}.up.railway.app",
                f"https://gra-prototype-production-{project_id[:4]}.up.railway.app",
                f"https://backend-production-{project_id[:4]}.up.railway.app"
            ]
            
            print("\n🧪 Testing possible URLs...")
            for url in patterns:
                print(f"   Testing: {url}")
                try:
                    response = requests.get(url, timeout=5)
                    if response.status_code == 200:
                        data = response.json()
                        if "GRA" in str(data):
                            print(f"   ✅ FOUND! Your app is at: {url}")
                            return url
                except:
                    pass
                print(f"   ❌ Not this one")
            
        except Exception as e:
            print(f"   ❌ Could not parse project ID: {e}")
    
    print("\n📋 Manual Steps:")
    print("1. Go to your Railway dashboard")
    print("2. Find your gra-prototype project")
    print("3. Look for the public URL")
    print("4. Test it by opening in browser")
    
    return None

def test_url():
    """Test a Railway URL"""
    print("\n🧪 Test Your Railway URL")
    print("-" * 30)
    
    url = input("Enter your Railway URL: ").strip()
    if not url:
        return
    
    if not url.startswith('http'):
        url = 'https://' + url
    
    url = url.rstrip('/')
    
    print(f"\n🔍 Testing: {url}")
    
    try:
        # Health check
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check passed!")
            print(f"   Response: {data}")
            
            # Test API docs
            print(f"\n📚 API Documentation: {url}/docs")
            
            # Test sample data loading
            print(f"\n📊 Testing sample data loading...")
            response = requests.post(f"{url}/ingest-sample", timeout=15)
            if response.status_code == 200:
                print(f"✅ Sample data loaded!")
            else:
                print(f"⚠️  Sample data loading issue: {response.status_code}")
            
            # Test query
            print(f"\n🤖 Testing query processing...")
            test_query = {"query": "What is RAG?", "context": "Testing"}
            response = requests.post(f"{url}/query", json=test_query, timeout=15)
            if response.status_code == 200:
                print(f"✅ Query processing works!")
            else:
                print(f"⚠️  Query processing issue: {response.status_code}")
            
            print(f"\n🎉 Your GRA Prototype is working!")
            print(f"🌐 Live URL: {url}")
            print(f"📚 API Docs: {url}/docs")
            
        else:
            print(f"❌ URL not responding: HTTP {response.status_code}")
            
    except Exception as e:
        print(f"❌ Connection error: {e}")
        print(f"\n💡 Possible issues:")
        print(f"   • App is still starting up (wait 2-3 minutes)")
        print(f"   • Deployment failed (check Railway logs)")
        print(f"   • Wrong URL (check Railway dashboard)")

def main():
    """Main function"""
    print("🎯 What would you like to do?")
    print("1. Find my Railway URL")
    print("2. Test a Railway URL")
    print("3. Both")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == "1":
        check_railway_deployment()
    elif choice == "2":
        test_url()
    elif choice == "3":
        url = check_railway_deployment()
        if not url:
            test_url()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()