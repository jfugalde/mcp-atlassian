# Quick Start Guide

## Set Environment Variables

### Option 1: Create .env file (Recommended)

```bash
cd scripts/shopify-analysis

# Create .env file from example
cat > .env << 'ENVFILE'
SHOPIFY_ACCESS_TOKEN="paste_your_token_here"
SHOPIFY_SHOP_DOMAIN="macross-pharma.myshopify.com"
PAGESPEED_INSIGHTS_API_KEY="paste_your_key_here"
ENVFILE
```

Then edit `.env` and replace the placeholder values with your actual tokens.

### Option 2: Export in Terminal

**macOS/Linux (zsh/bash):**
```bash
export SHOPIFY_ACCESS_TOKEN="shpat_xxxxxxxxxxxxx"
export SHOPIFY_SHOP_DOMAIN="macross-pharma.myshopify.com"
export PAGESPEED_INSIGHTS_API_KEY="AIzaSyxxxxxxxxxxxxx"
```

**Windows PowerShell:**
```powershell
$env:SHOPIFY_ACCESS_TOKEN="shpat_xxxxxxxxxxxxx"
$env:SHOPIFY_SHOP_DOMAIN="macross-pharma.myshopify.com"
$env:PAGESPEED_INSIGHTS_API_KEY="AIzaSyxxxxxxxxxxxxx"
```

## Run Analysis

```bash
cd scripts/shopify-analysis
pip install -r requirements.txt
python run_analysis.py
```

See SETUP.md for detailed instructions on getting your tokens.
