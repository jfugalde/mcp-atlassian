# RYU Website Improvements Plan

**Generated**: 2025-12-02  
**Based on**: Growth Strategy 2025-2026  
**Priority**: High - Foundation for service launches

---

## 1. Executive Summary

- **Current State**: React/Vite site with 4 services, 3 case studies, basic automation showcase
- **Gap**: Missing new service offerings (Automation Audit, Metrics Dashboard, Healthcare Package), no pricing visibility, no lead magnets
- **Goal**: Align website with growth strategy, add conversion-focused elements, support service launches
- **Timeline**: 3-4 weeks (phased approach)

---

## 2. Website Improvements Required

### 2.1 Service Catalog Updates

**Current Services** (in `dataStructures.js`):
1. Business Digitalization
2. Audit Kits
3. Automation Packs
4. Ecommerce OS Builds

**New Services to Add** (from Growth Strategy):
1. **Automation Audit + Quick Wins** ($800-$1,500 MXN)
   - Entry offer, low-ticket
   - 2-hour discovery, audit report, 1 automation
   - Target: Ecommerce/retail brands (50-200 employees)

2. **Metrics Dashboard Setup** ($1,200-$2,000 MXN)
   - Entry offer, quick win
   - Unified dashboard (Looker Studio), email reports, alerts
   - Target: Ecommerce brands wanting visibility

3. **Ecommerce Operations Automation Package** ($1,500-$2,500 + retainer)
   - Core project, mid-ticket
   - 5-7 n8n workflows, training, 30-day support
   - Target: Active marketing operations

4. **Healthcare Lead Automation Package** ($2,000-$3,500 + retainer)
   - Core project, healthcare vertical
   - WhatsApp bot, CRM integration, analytics
   - Target: Pharmacies, healthcare providers

5. **Automation Studio Retainer** ($2,000-$5,000/mo)
   - Flagship offer, high-LTV
   - Monthly automation sprints, ongoing optimization
   - Target: Growing ecommerce brands (100-500 employees)

**Action Items**:
- Update `dataStructures.js` with new services
- Add pricing ranges (displayed conditionally or on service detail pages)
- Create service detail pages for new services
- Update ServicesGrid component to handle 9 services (currently 4)

---

### 2.2 Case Studies Enhancement

**Current Case Studies**:
1. Cosmetics Brand (Solo Founder)
2. Fashion Brand (Small Team)
3. Electronics Brand (Solo Founder)

**New Case Studies to Add**:
1. **Suppathletik Case Study** (from RYU-WF-2-1)
   - Ecommerce automation showcase
   - Metrics: Time saved, automation workflows, ROI
   - Extract from workflow improvement tickets

2. **Macross Farma Case Study** (from RYU-WF-2-2)
   - Healthcare automation showcase
   - Metrics: Leads automated, conversion rate, time saved
   - Extract from FM project (post-completion)

**Action Items**:
- Add case studies to `dataStructures.js`
- Create case study detail pages
- Add metrics visualization
- Link to service packages (Healthcare Package from Macross)

---

### 2.3 Pricing & Transparency

**Current State**: No pricing visible on website

**Improvements Needed**:
- Add pricing ranges to service cards (optional toggle)
- Create "Pricing" page with all service tiers
- Add "Starting at $X" badges to service cards
- Display retainer pricing clearly

**Action Items**:
- Create `PricingPage.jsx` component
- Add pricing data to `dataStructures.js`
- Update service cards to show pricing (optional)
- Add pricing FAQ section

---

### 2.4 Lead Magnets & Conversion

**Current State**: Basic contact form, no lead magnets

**Improvements Needed**:
- **Automation Audit Landing Page** (for Experiment 1)
  - Dedicated landing page for Automation Audit offer
  - Form with qualification questions
  - Lead magnet: "5 Automations Every Ecommerce Brand Needs" (PDF)
  
- **Workflow Template Hub Waitlist** (for Experiment 2)
  - Landing page with waitlist signup
  - 3 free templates as lead magnet
  - Email sequence integration

- **Healthcare Package Landing Page** (for Experiment 3)
  - Dedicated page for healthcare automation
  - Macross case study preview
  - Lead magnet: "Healthcare Automation Playbook"

**Action Items**:
- Create landing page components
- Add lead magnet download functionality
- Integrate with email service (Web3Forms or Mailchimp)
- Add analytics tracking (GA4 events)

---

### 2.5 Content & SEO

**Current State**: Basic content, no blog

**Improvements Needed**:
- **Blog Section** (for content marketing)
  - Blog listing page
  - Blog post detail pages
  - Categories: Automation, Case Studies, Ecommerce Tips
  - Initial posts:
    - "5 Automations Every Ecommerce Brand Needs"
    - "How to Automate Daily Metrics Collection"
    - "Healthcare Lead Automation: Macross Case Study"
    - "From Spreadsheets to Automation: A Guide"

- **SEO Enhancements**:
  - Meta descriptions for all pages
  - Open Graph tags
  - Structured data (JSON-LD)
  - Sitemap generation
  - Robots.txt optimization

**Action Items**:
- Create blog components (BlogList, BlogPost)
- Add blog data structure
- Implement SEO meta tags
- Add structured data

---

### 2.6 International Expansion (Japan)

**Current State**: i18n support exists (en, es, ja) but content not fully translated

**Improvements Needed**:
- Complete Japanese translations
- Japan-specific case studies (future)
- Japan market messaging
- Localized pricing (JPY)

**Action Items**:
- Review and complete Japanese translations
- Add Japan market section (future)
- Update pricing for JPY display

---

### 2.7 Technical Improvements

**Performance**:
- Image optimization (WebP, lazy loading)
- Code splitting for routes
- Bundle size optimization
- Lighthouse score >90

**Analytics**:
- GA4 event tracking (button clicks, form submissions, downloads)
- Conversion tracking (service inquiries, lead magnet downloads)
- Heatmap integration (optional: Hotjar)

**Accessibility**:
- ARIA labels
- Keyboard navigation
- Screen reader testing
- WCAG 2.1 AA compliance

**Action Items**:
- Audit current performance
- Implement optimizations
- Set up GA4 events
- Accessibility audit and fixes

---

## 3. Implementation Phases

### Phase 1: Foundation (Week 1-2)
- Add new services to data structures
- Create service detail pages
- Add pricing data
- Update ServicesGrid component

### Phase 2: Conversion (Week 2-3)
- Create Automation Audit landing page
- Add lead magnet functionality
- Implement email integration
- Add analytics tracking

### Phase 3: Content (Week 3-4)
- Create blog section
- Write initial blog posts
- SEO enhancements
- Performance optimization

### Phase 4: Enhancement (Week 4+)
- Add Suppathletik case study
- Add Macross case study (post-completion)
- Complete Japanese translations
- Accessibility improvements

---

## 4. Success Metrics

**Conversion Metrics**:
- Form submission rate → Target: >3%
- Lead magnet downloads → Target: 50+/month
- Service page views → Target: 200+/month
- Bounce rate → Target: <50%

**Engagement Metrics**:
- Average session duration → Target: >2 minutes
- Pages per session → Target: >3
- Blog post reads → Target: 100+/month

**Business Metrics**:
- Qualified leads from website → Target: 5-10/month
- Service inquiries → Target: 3-5/month
- CAC from website → Target: <$3,000 MXN

---

## 5. Dependencies

- **Content**: Need case study data from Suppathletik and Macross projects
- **Design**: May need new icons/illustrations for new services
- **Backend**: Email service setup (Web3Forms or Mailchimp)
- **Analytics**: GA4 property setup and configuration

---

**Document Version**: 1.0  
**Last Updated**: 2025-12-02

