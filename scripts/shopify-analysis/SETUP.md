# Setup Guide - Shopify Storefront Analysis

Complete guide to set up and configure the Shopify storefront analysis tools.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Environment Variables Setup](#environment-variables-setup)
- [Getting Your Access Token](#getting-your-access-token)
- [Getting PageSpeed Insights API Key](#getting-pagespeed-insights-api-key-optional)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before you begin, ensure you have:

- Python 3.10 or higher installed
- `pip` (usually comes with Python)
- Access to your Shopify store admin
- (Optional) Google Cloud account for PageSpeed Insights API

---

## Quick Start

If you just want to get started quickly:

### Option A: Automated Setup (macOS/Linux)

```bash
# 1. Navigate to the analysis directory
cd scripts/shopify-analysis

# 2. Run the setup script (creates venv and installs dependencies)
./setup_venv.sh

# 3. Activate virtual environment (if not already active)
source venv/bin/activate

# 4. Create .env file
cat > .env << EOF
SHOPIFY_ACCESS_TOKEN="your_token_here"
SHOPIFY_SHOP_DOMAIN="macross-pharma.myshopify.com"
PAGESPEED_INSIGHTS_API_KEY="your_key_here"
EOF

# 5. Edit .env and add your actual tokens (see sections below)

# 6. Test the connection
python local_test.py
```

### Option B: Manual Setup

```bash
# 1. Navigate to the analysis directory
cd scripts/shopify-analysis

# 2. Create and activate virtual environment
python -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Create .env file
cat > .env << EOF
SHOPIFY_ACCESS_TOKEN="your_token_here"
SHOPIFY_SHOP_DOMAIN="macross-pharma.myshopify.com"
PAGESPEED_INSIGHTS_API_KEY="your_key_here"
EOF

# 5. Edit .env and add your actual tokens (see sections below)

# 6. Test the connection
python local_test.py
```

**Note:** Always activate the virtual environment before running scripts. You'll see `(venv)` in your terminal prompt when it's active.

---

## Virtual Environment Setup

Using a virtual environment (venv) is **strongly recommended** to keep dependencies isolated and avoid conflicts with other Python projects.

### Create Virtual Environment

```bash
cd scripts/shopify-analysis

# Create virtual environment
python -m venv venv

# Or if you need to specify Python 3 explicitly:
python3 -m venv venv
```

### Activate Virtual Environment

**On macOS/Linux:**

```bash
source venv/bin/activate
```

**On Windows (PowerShell):**

```powershell
venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**

```cmd
venv\Scripts\activate.bat
```

You'll know it's activated when you see `(venv)` at the beginning of your terminal prompt:

```bash
(venv) user@computer:~/scripts/shopify-analysis$
```

### Install Dependencies

Once the virtual environment is activated:

```bash
# Upgrade pip (recommended)
pip install --upgrade pip

# Install project dependencies
pip install -r requirements.txt
```

### Deactivate Virtual Environment

When you're done working:

```bash
deactivate
```

### Verify Installation

Check that packages are installed:

```bash
pip list
```

You should see `httpx` and `python-dotenv` in the list.

**Important:** Always activate the virtual environment before running any analysis scripts!

---

## Environment Variables Setup

The analysis tools require three environment variables. Choose the setup method that works best for you.

### Required Variables

| Variable                     | Required   | Description                                                              |
| ---------------------------- | ---------- | ------------------------------------------------------------------------ |
| `SHOPIFY_ACCESS_TOKEN`       | ✅ Yes      | Your Shopify Admin API access token                                      |
| `SHOPIFY_SHOP_DOMAIN`        | ⚠️ Optional | Your shop domain (defaults to `macross-pharma.myshopify.com`)            |
| `PAGESPEED_INSIGHTS_API_KEY` | ⚠️ Optional | Google PageSpeed Insights API key (only needed for performance analysis) |

### Method 1: Using a .env File (Recommended)

This is the easiest and most secure method. The scripts automatically load variables from a `.env` file.

#### Step 1: Create the .env file

```bash
cd scripts/shopify-analysis

# Create from template (if .env.example exists)
cp .env.example .env

# Or create manually
cat > .env << EOF
SHOPIFY_ACCESS_TOKEN="shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
SHOPIFY_SHOP_DOMAIN="macross-pharma.myshopify.com"
PAGESPEED_INSIGHTS_API_KEY="AIzaSyxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
EOF
```

#### Step 2: Edit the .env file

Open `.env` in your preferred editor and replace the placeholder values with your actual tokens:

```bash
# Using nano
nano .env

# Using vim
vim .env

# Using VS Code
code .env
```

#### Step 3: Verify it works

```bash
python -c "from auth import get_access_token; print('✅ Token loaded!' if get_access_token() else '❌ Token not found')"
```

**Security Note:** The `.env` file is automatically ignored by git (via `.gitignore`) to keep your tokens secure. Never commit this file to version control.

---

### Method 2: Export in Terminal (Temporary)

Set variables in your current terminal session. These will only last until you close the terminal.

#### macOS/Linux (zsh/bash)

```bash
export SHOPIFY_ACCESS_TOKEN="shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export SHOPIFY_SHOP_DOMAIN="macross-pharma.myshopify.com"
export PAGESPEED_INSIGHTS_API_KEY="AIzaSyxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

#### Windows PowerShell

```powershell
$env:SHOPIFY_ACCESS_TOKEN="shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
$env:SHOPIFY_SHOP_DOMAIN="macross-pharma.myshopify.com"
$env:PAGESPEED_INSIGHTS_API_KEY="AIzaSyxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

#### Windows Command Prompt

```cmd
set SHOPIFY_ACCESS_TOKEN=shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
set SHOPIFY_SHOP_DOMAIN=macross-pharma.myshopify.com
set PAGESPEED_INSIGHTS_API_KEY=AIzaSyxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Verify they're set

```bash
# macOS/Linux
echo $SHOPIFY_ACCESS_TOKEN

# Windows PowerShell
echo $env:SHOPIFY_ACCESS_TOKEN

# Windows CMD
echo %SHOPIFY_ACCESS_TOKEN%
```

---

### Method 3: Add to Shell Profile (Persistent)

Add exports to your shell profile so they're available in every terminal session.

#### For zsh (macOS default)

```bash
# Edit your ~/.zshrc file
nano ~/.zshrc

# Add these lines at the end:
export SHOPIFY_ACCESS_TOKEN="shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export SHOPIFY_SHOP_DOMAIN="macross-pharma.myshopify.com"
export PAGESPEED_INSIGHTS_API_KEY="AIzaSyxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Save (Ctrl+O, Enter, Ctrl+X in nano)
# Then reload
source ~/.zshrc
```

#### For bash

```bash
# Edit your ~/.bashrc or ~/.bash_profile
nano ~/.bashrc

# Add the same export lines, then:
source ~/.bashrc
```

#### For PowerShell (Windows)

```powershell
# Edit your PowerShell profile
notepad $PROFILE

# Add these lines:
$env:SHOPIFY_ACCESS_TOKEN="shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
$env:SHOPIFY_SHOP_DOMAIN="macross-pharma.myshopify.com"
$env:PAGESPEED_INSIGHTS_API_KEY="AIzaSyxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Reload PowerShell or restart terminal
```

---

## Getting Your Access Token

You have two options to get a Shopify Admin API access token. **Option B (Private App) is recommended** for simplicity.

### Option A: Using the admin-app (OAuth)

This method uses the existing `admin-app` in this repository.

#### Step 1: Navigate to admin-app

```bash
cd admin-app
```

#### Step 2: Install dependencies

```bash
npm install
```

#### Step 3: Start the development server

```bash
npm run shopify app dev
```

#### Step 4: Follow the OAuth flow

1. The CLI will prompt you to install the app on your store
2. Follow the browser prompts to authorize the app
3. The access token will be stored in the app's session
4. Extract it from the app configuration or OAuth response

**Note:** This method requires the Shopify CLI and Node.js to be installed.

---

### Option B: Create a Private App (Recommended)

This is the easiest method and doesn't require any development setup.

#### Step 1: Access Shopify Admin

Go to your Shopify Admin: [https://admin.shopify.com/store/macross-pharma](https://admin.shopify.com/store/macross-pharma)

#### Step 2: Navigate to Apps Settings

1. Click **Settings** (gear icon in bottom left)
2. Click **Apps and sales channels**
3. Click **Develop apps** (top right)
4. Click **Create an app**

#### Step 3: Configure the App

1. **Name the app**: e.g., "Storefront Analysis" or "Macross Analysis Tool"
2. Click **Create app**

#### Step 4: Configure Admin API Scopes

1. Click **Configure Admin API scopes**
2. Enable the following scopes (these are the minimum required):

   **Required Scopes:**
   - `read_apps` - To query installed apps
   - `read_themes` - To query theme information
   - `read_products` - To query product data
   - `read_orders` - To query order data
   - `read_storefront_access_tokens` - To query storefront tokens

   **Optional Scopes (for extended analysis):**
   - `read_customers` - For customer analytics
   - `read_analytics` - For store analytics
   - `read_content` - For content analysis

3. Click **Save**

#### Step 5: Install the App

1. Click **Install app** (top right)
2. Review the permissions and click **Install**

#### Step 6: Copy the Access Token

1. After installation, you'll see the **Admin API access token**
2. Click **Reveal token once** or **Copy token**
3. The token starts with `shpat_` followed by a long string
4. **Important:** Copy this token immediately - you won't be able to see it again!

#### Step 7: Add Token to Your Configuration

Paste the token into your `.env` file:

```bash
SHOPIFY_ACCESS_TOKEN="shpat_your_actual_token_here"
```

**Security Warning:** Never share your access token or commit it to version control. Treat it like a password.

---

## Getting PageSpeed Insights API Key (Optional)

The PageSpeed Insights API key is only needed if you want to run performance analysis. The analysis tools will work without it, but performance metrics won't be available.

### Step 1: Access Google Cloud Console

Go to [Google Cloud Console](https://console.cloud.google.com/)

### Step 2: Create or Select a Project

1. Click the project dropdown at the top
2. Click **New Project** or select an existing project
3. If creating new: Enter project name (e.g., "Shopify Analysis") and click **Create**

### Step 3: Enable PageSpeed Insights API

1. Go to **APIs & Services** → **Library** (or search "APIs" in the top search bar)
2. Search for "PageSpeed Insights API"
3. Click on **PageSpeed Insights API**
4. Click **Enable**

### Step 4: Create API Key

1. Go to **APIs & Services** → **Credentials**
2. Click **Create Credentials** → **API Key**
3. Copy the API key (it starts with `AIzaSy`)

### Step 5: (Recommended) Restrict the API Key

For security, restrict the API key to only PageSpeed Insights API:

1. Click **Restrict key** (or edit the key)
2. Under **API restrictions**, select **Restrict key**
3. Check only **PageSpeed Insights API**
4. Click **Save**

### Step 6: Add to Configuration

Add the API key to your `.env` file:

```bash
PAGESPEED_INSIGHTS_API_KEY="AIzaSy_your_actual_key_here"
```

**Note:** The free tier of PageSpeed Insights API allows 25,000 requests per day, which is more than enough for testing.

---

## Verification

After setting up your environment variables, verify everything works:

### Quick Test

```bash
cd scripts/shopify-analysis
python local_test.py
```

Select option **5** (Test API Connection) to verify your setup.

### Manual Verification

```bash
# Test token loading
python -c "from auth import get_access_token, get_shop_domain; print(f'Token: {\"✅ Found\" if get_access_token() else \"❌ Missing\"}'); print(f'Domain: {get_shop_domain()}')"

# Test API connection
python -c "
from auth import create_graphql_client, execute_graphql_query
client = create_graphql_client()
result = execute_graphql_query(client, '{ shop { name } }')
print(f'✅ Connected to: {result.get(\"shop\", {}).get(\"name\", \"Unknown\")}')
client.close()
"
```

### Run a Quick Analysis

```bash
python query_apps.py
```

If this runs without errors and shows your installed apps, everything is configured correctly!

---

## Troubleshooting

### Error: "Access token is required"

**Problem:** The `SHOPIFY_ACCESS_TOKEN` environment variable is not set or not loaded.

**Solutions:**

1. Check that your `.env` file exists in `scripts/shopify-analysis/`
2. Verify the token is in the file: `cat .env | grep SHOPIFY_ACCESS_TOKEN`
3. Make sure you're running scripts from the correct directory
4. If using terminal exports, verify with `echo $SHOPIFY_ACCESS_TOKEN`

### Error: "read_apps scope required"

**Problem:** Your access token doesn't have the `read_apps` scope.

**Solutions:**

1. Go back to your Private App configuration in Shopify Admin
2. Click **Configure Admin API scopes**
3. Enable `read_apps` scope
4. Click **Save** and reinstall the app
5. Copy the new access token

**Note:** The `read_apps` scope may require approval from Shopify Support for some stores. If you see an approval message, follow the prompts.

### Error: "Invalid API version" or "API version not supported"

**Problem:** The API version in use might be outdated.

**Solutions:**

1. Check `auth.py` for the API version setting
2. Update to a recent API version (e.g., `2025-01` or `2025-10`)
3. Some queries may need adjustment for newer API versions

### Error: "Connection refused" or "Network error"

**Problem:** Network connectivity issues or incorrect shop domain.

**Solutions:**

1. Verify your shop domain is correct: `echo $SHOPIFY_SHOP_DOMAIN`
2. Check internet connectivity
3. Verify the shop domain format: `your-shop.myshopify.com` (not `your-shop.com`)

### Error: "PageSpeed Insights API key invalid"

**Problem:** The PageSpeed Insights API key is incorrect or not enabled.

**Solutions:**

1. Verify the API key in Google Cloud Console
2. Check that PageSpeed Insights API is enabled for your project
3. Verify the API key is not restricted incorrectly
4. Test the API key: `curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://example.com&key=YOUR_KEY"`

### Performance Analysis Not Working

**Problem:** Performance analysis requires a PageSpeed Insights API key.

**Solutions:**

1. The performance analysis is optional - other analyses will work without it
2. Follow the [PageSpeed Insights API Key setup](#getting-pagespeed-insights-api-key-optional) section
3. Or skip performance analysis and use other features

### Import Errors

**Problem:** Python dependencies not installed or virtual environment not activated.

**Solutions:**

1. **Make sure virtual environment is activated:**

   ```bash
   # Check if venv is active (you should see (venv) in prompt)
   # If not, activate it:
   source venv/bin/activate  # macOS/Linux
   # or
   venv\Scripts\activate  # Windows
   ```

2. **Install dependencies:**

   ```bash
   cd scripts/shopify-analysis
   pip install -r requirements.txt
   ```

3. **If virtual environment doesn't exist, create it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   pip install -r requirements.txt
   ```

4. **Verify installation:**

   ```bash
   pip list | grep httpx
   pip list | grep python-dotenv
   ```

---

## Next Steps

Once your setup is verified:

**Remember:** Always activate your virtual environment first!

```bash
cd scripts/shopify-analysis
source venv/bin/activate  # macOS/Linux
# or venv\Scripts\activate on Windows
```

Then you can:

1. **Run Interactive Testing:**

   ```bash
   python local_test.py
   ```

2. **Run Quick Analysis:**

   ```bash
   python run_analysis.py
   ```

3. **Run Deep App Analysis:**

   ```bash
   python app_analyzer.py
   ```

4. **View Reports:**

   Check `docs/shopify-analysis/` for generated reports

---

## Security Best Practices

1. **Never commit `.env` files** - They're already in `.gitignore`
2. **Rotate tokens regularly** - Regenerate access tokens periodically
3. **Use minimum required scopes** - Only enable scopes you actually need
4. **Restrict API keys** - Limit PageSpeed Insights API key to specific APIs
5. **Store tokens securely** - Use `.env` files or secure credential managers
6. **Don't share tokens** - Treat access tokens like passwords

---

## Support

If you encounter issues not covered here:

1. Check the [README.md](README.md) for general information
2. Review error messages carefully - they often contain helpful hints
3. Verify all prerequisites are met
4. Ensure you're using the latest version of the scripts

---

**Last Updated:** 2025-01
