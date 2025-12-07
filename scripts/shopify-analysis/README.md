# Shopify Storefront Analysis

Comprehensive analysis tools for Shopify storefronts, including installed apps, theme information, store configuration, and performance metrics.

## Setup

### 1. Create Virtual Environment (Recommended)

Using a virtual environment keeps dependencies isolated and avoids conflicts.

**Quick Setup (macOS/Linux):**

```bash
cd scripts/shopify-analysis
./setup_venv.sh
source venv/bin/activate
```

**Manual Setup:**

```bash
cd scripts/shopify-analysis
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

**Important:** Always activate the virtual environment before running scripts. You'll see `(venv)` in your terminal prompt when it's active.

### 2. Configure Environment Variables

**Recommended:** Create a `.env` file (see [SETUP.md](SETUP.md) for detailed instructions):

```bash
cd scripts/shopify-analysis
cp .env.example .env
# Then edit .env and add your actual tokens
```

**Alternative:** Set environment variables in your terminal:

```bash
# In terminal (macOS/Linux):
export SHOPIFY_ACCESS_TOKEN="your_access_token_here"
export SHOPIFY_SHOP_DOMAIN="macross-pharma.myshopify.com"
export PAGESPEED_INSIGHTS_API_KEY="your_api_key_here"  # Optional

# In PowerShell (Windows):
$env:SHOPIFY_ACCESS_TOKEN="your_access_token_here"
$env:SHOPIFY_SHOP_DOMAIN="macross-pharma.myshopify.com"
$env:PAGESPEED_INSIGHTS_API_KEY="your_api_key_here"  # Optional
```

See [SETUP.md](SETUP.md) for complete setup instructions.

### 3. Get Access Token

You have two options:

#### Option A: Use the admin-app (OAuth)

1. Navigate to `admin-app/` directory
2. Run `npm run shopify app dev`
3. Install the app on your store
4. Extract the access token from the OAuth flow

#### Option B: Create a Private App

1. Go to Shopify Admin → Settings → Apps and sales channels
2. Click "Develop apps" → "Create an app"
3. Configure the following scopes:
   - `read_apps`
   - `read_themes`
   - `read_products`
   - `read_orders`
   - `read_storefront_access_tokens`
4. Install the app and copy the Admin API access token

### 4. Get PageSpeed Insights API Key (Optional)

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable "PageSpeed Insights API"
4. Create credentials (API Key)
5. Copy the API key

## Usage

### Interactive Local Testing (Recommended)

For local testing and development, use the interactive interface:

```bash
cd scripts/shopify-analysis
python local_test.py
```

This provides an interactive menu to:
- Test API connection
- Run quick analysis (apps, theme, store config)
- Run **deep app analysis** (security, cost, performance impact)
- Run performance analysis (PageSpeed Insights)
- Run full comprehensive analysis
- View saved reports

### Run Complete Analysis (Non-Interactive)

```bash
python run_analysis.py
```

This will:
1. Query all installed apps
2. Get theme information
3. Retrieve store configuration
4. Analyze performance (if API key is set)
5. Generate a comprehensive markdown report

### Run Individual Scripts

```bash
# Deep app analysis (security, cost, performance impact)
python app_analyzer.py

# Query installed apps only
python query_apps.py

# Query theme information only
python query_theme.py

# Query store configuration only
python query_store_config.py

# Analyze performance only
python performance_analysis.py

# Generate report from existing data
python generate_report.py
```

## Output

All analysis data is saved to `docs/shopify-analysis/`:

- `installed_apps.json` - List of installed apps with details
- `theme_info.json` - Theme information
- `store_config.json` - Store configuration
- `performance_analysis.json` - Performance metrics
- `deep_app_analysis.json` - Deep app analysis (security, cost, performance)
- `deep_app_analysis_report.md` - Deep app analysis report
- `macross-pharma-analysis.md` - Comprehensive markdown report

## Report Contents

The generated report includes:

1. **Executive Summary** - Overview of findings
2. **Store Configuration** - Plan, features, currency, timezone
3. **Theme Information** - Published theme and all themes
4. **Installed Apps** - Complete inventory with scopes and subscriptions
5. **Deep App Analysis** - Security scores, cost analysis, performance impact
6. **Performance Analysis** - Core Web Vitals and Lighthouse scores
7. **Recommendations** - Actionable optimization suggestions

### Deep App Analysis Features

The deep app analysis (`app_analyzer.py`) provides:

- **Security Analysis**: Identifies high-risk permissions, security scores
- **Cost Analysis**: Calculates total monthly/annual costs including subscriptions and usage
- **Performance Impact**: Assesses potential performance impact based on app capabilities
- **Recommendations**: Actionable suggestions for each app
- **Overall Scoring**: Combined score for each app (0-100)

## Troubleshooting

### "Access token is required" error

Make sure you've set the `SHOPIFY_ACCESS_TOKEN` environment variable or have it in your `.env` file.

### "read_apps scope required" error

The `read_apps` scope requires approval from Shopify Support. You can:
1. Request approval through Partner Dashboard
2. Or use a private app with the scope enabled

### Performance analysis fails

- Ensure you have a valid PageSpeed Insights API key
- Check that your storefront is publicly accessible
- Verify the page paths are correct

## Notes

- The `read_apps` scope may require approval from Shopify Support
- Performance analysis uses Google PageSpeed Insights API (free tier available)
- All GraphQL queries are validated against Shopify's schema
- The analysis follows Shopify's performance testing methodology (weighted scores)

