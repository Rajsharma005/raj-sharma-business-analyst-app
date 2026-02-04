### 1. Executive Summary
- **Business context:** A mid-size telecom operator is seeing churn rise for monthly plan users over the last two quarters, coinciding with stalled revenue growth. The business depends on recurring subscriptions, so churn is directly eroding future cash flows and brand trust.
- **Why this problem matters now:** Two consecutive quarters of churn acceleration indicates a structural issue rather than seasonal noise. If left unaddressed, customer lifetime value will decline, acquisition costs will rise, and competitive pressure will intensify.
- **High-level outcome of the analysis:** The analysis points to a combination of service experience gaps and plan-value misalignment for monthly users, with targeted retention levers expected to stabilize churn and re-ignite revenue growth within one to two quarters.

---

### 2. Problem Classification (using problem_classifier logic)
- **Primary problem category:** Churn
- **Secondary sub-problems:**
  - Customer experience degradation (service reliability and support responsiveness)
  - Pricing and plan-value misalignment for monthly subscribers
  - Competitive switching due to promotional offers
- **Why this is NOT just a “data problem” but a business decision problem:** The core issue is whether to invest in retention levers (service improvements, plan redesign, targeted offers) or continue spending on acquisition to replace churned users. This is a strategic decision with material revenue and brand implications.

---

### 3. Domain Mapping (using domain_mapper logic)
- **Primary business domain(s):** Telecom (subscription services)
- **Supporting domains:** Customer Retention, Network Operations, Billing & Plans
- **Industry-specific considerations for telecom:**
  - Churn can be driven by network reliability, coverage gaps, or service outages.
  - Monthly plans are highly price-sensitive and respond quickly to competitive promotions.
  - Switching costs are low, so customer experience and perceived value are decisive.

---

### 4. KPI Mapping (using kpi_mapper logic)
- **Gross Revenue Churn %**
  - **Definition:** Revenue lost from churned customers divided by starting recurring revenue.
  - **Why it matters:** Directly quantifies revenue erosion.
  - **Leading/Lagging:** Lagging
  - **Data source:** Billing and subscription ledger
  - **Risk if misunderstood:** Underestimates urgency by ignoring revenue impact.

- **Logo Churn %**
  - **Definition:** Customers lost divided by starting customer base.
  - **Why it matters:** Signals customer attrition independent of revenue tier.
  - **Leading/Lagging:** Lagging
  - **Data source:** Customer master and account status records
  - **Risk if misunderstood:** Overemphasizes low-value churn if not segmented.

- **Plan Downgrade Rate**
  - **Definition:** Percentage of customers moving from monthly to lower-value plans.
  - **Why it matters:** Indicates value erosion before full churn.
  - **Leading/Lagging:** Leading
  - **Data source:** Plan change history
  - **Risk if misunderstood:** Misses early warning signals of churn.

- **Network Reliability (Service Disruption Rate)**
  - **Definition:** Incidents per 1,000 subscribers per month.
  - **Why it matters:** Service stability is a primary churn driver in telecom.
  - **Leading/Lagging:** Leading
  - **Data source:** Network operations incident logs
  - **Risk if misunderstood:** Blames churn on pricing when reliability is the root cause.

- **Support Resolution Time**
  - **Definition:** Average time to resolve customer issues.
  - **Why it matters:** Long resolution times reduce satisfaction and increase churn risk.
  - **Leading/Lagging:** Leading
  - **Data source:** Customer support system
  - **Risk if misunderstood:** Underestimates experience-related churn risk.

- **Retention Offer Uptake**
  - **Definition:** Percentage of targeted churn-risk customers accepting retention offers.
  - **Why it matters:** Measures effectiveness of save initiatives.
  - **Leading/Lagging:** Leading
  - **Data source:** Retention campaign records
  - **Risk if misunderstood:** Confuses short-term saves with long-term loyalty.

---

### 5. Hypothesis Generation (using hypothesis_generator logic)
1. **Hypothesis:** Network service disruptions are driving churn among monthly plan users.  
   - **Linked KPI(s):** Service Disruption Rate, Logo Churn %  
   - **Rationale:** Monthly users have low switching costs and respond quickly to service quality issues.  
   - **Test approach:** Compare churn rates in high-disruption vs low-disruption regions.  
   - **Null hypothesis:** Churn rates are similar regardless of disruption levels.

2. **Hypothesis:** Monthly plan pricing is no longer competitive, leading to value-based churn.  
   - **Linked KPI(s):** Gross Revenue Churn %, Plan Downgrade Rate  
   - **Rationale:** Competitive pricing shifts can trigger churn in price-sensitive cohorts.  
   - **Test approach:** Benchmark churn against competitor pricing changes and promotional periods.  
   - **Null hypothesis:** Pricing differences do not significantly impact churn.

3. **Hypothesis:** Support resolution time increases correlate with churn spikes.  
   - **Linked KPI(s):** Support Resolution Time, Logo Churn %  
   - **Rationale:** Friction in customer support reduces satisfaction and loyalty.  
   - **Test approach:** Correlate support turnaround time with churn by segment.  
   - **Null hypothesis:** Support resolution time has no measurable impact on churn.

4. **Hypothesis:** High-value monthly customers are downgrading before fully churning.  
   - **Linked KPI(s):** Plan Downgrade Rate, Gross Revenue Churn %  
   - **Rationale:** Downgrades are a leading signal of dissatisfaction.  
   - **Test approach:** Track downgrade cohorts and subsequent churn probability.  
   - **Null hypothesis:** Downgrades are unrelated to churn behavior.

5. **Hypothesis:** Retention offers are poorly targeted, reducing save effectiveness.  
   - **Linked KPI(s):** Retention Offer Uptake, Gross Revenue Churn %  
   - **Rationale:** Blanket offers dilute impact and increase cost.  
   - **Test approach:** Compare churn outcomes for targeted vs non-targeted cohorts.  
   - **Null hypothesis:** Targeting strategy does not affect churn outcomes.

6. **Hypothesis:** Churn is concentrated in specific regions with coverage gaps.  
   - **Linked KPI(s):** Service Disruption Rate, Logo Churn %  
   - **Rationale:** Localized coverage issues can drive regional churn spikes.  
   - **Test approach:** Geographic segmentation of churn and coverage quality.  
   - **Null hypothesis:** Churn is evenly distributed across regions.

---

### 6. Insight Simulation (NO real data)
- **Validated hypotheses:**
  - Network service disruptions correlate strongly with churn in two high-density regions.
  - Monthly plan pricing is less competitive in the lowest ARPU segment, increasing churn.
  - Downgrades precede churn by one to two months in high-value cohorts.
- **Rejected hypotheses:**
  - Support resolution time is stable and not a primary driver.
  - Retention offers, while modestly effective, are not the main lever.
- **Assumptions:**
  - Service quality signals are accurate and comparable across regions.
  - Competitor pricing benchmarks reflect true customer alternatives.
- **Business insights:**
  - Churn is not uniform; it is concentrated in regions with service reliability issues.
  - Price sensitivity among monthly users is high; plan value perception is weak.
  - Early downgrade behavior provides a window for proactive retention.

---

### 7. Recommendations (using recommendation_engine logic)
**Quick wins**
- **Action statement:** Launch regional retention outreach in high-disruption zones with targeted credits.  
  - **Linked hypothesis:** Service disruptions drive churn.  
  - **Expected business impact:** Immediate churn stabilization in highest-risk regions.  
  - **Effort level:** Low  
  - **Risk & dependencies:** Requires coordinated customer communication.  
  - **Priority:** P1  
  - **Owner:** Customer Experience

- **Action statement:** Trigger save offers at first downgrade event for monthly users.  
  - **Linked hypothesis:** Downgrades precede churn.  
  - **Expected business impact:** Reduce churn conversion from downgrade cohorts.  
  - **Effort level:** Low  
  - **Risk & dependencies:** Requires clear eligibility rules.  
  - **Priority:** P1  
  - **Owner:** Retention

**Strategic bets**
- **Action statement:** Redesign monthly plan bundles to improve value perception.  
  - **Linked hypothesis:** Pricing is no longer competitive.  
  - **Expected business impact:** Improve retention and ARPU over two quarters.  
  - **Effort level:** High  
  - **Risk & dependencies:** Requires pricing approvals and billing changes.  
  - **Priority:** P2  
  - **Owner:** Product & Pricing

- **Action statement:** Accelerate network investment in high-churn regions.  
  - **Linked hypothesis:** Service disruptions drive churn.  
  - **Expected business impact:** Structural churn reduction and brand improvement.  
  - **Effort level:** High  
  - **Risk & dependencies:** Capex commitment and execution timelines.  
  - **Priority:** P2  
  - **Owner:** Network Operations

**What NOT to do**
- Do not run blanket discounts across all monthly users; this dilutes margin without addressing root causes.
- Do not scale retention offers without segmentation; effectiveness will decline and costs will rise.

---

### 8. Executive Decision Roadmap
- **30 days:** Stabilize churn in high-disruption regions with targeted outreach; activate downgrade-triggered saves.
- **60 days:** Finalize revised monthly plan design and run controlled market pilots; confirm churn elasticity.
- **90 days:** Scale winning plan changes and commence network investment program.
- **Trade-offs considered:** Short-term credits versus long-term margin; targeted investment versus broad marketing spend.
- **Leadership decisions now:** Approve targeted credits, authorize plan redesign pilots, allocate capex for top-risk regions.
- **Decisions later:** Full-scale plan rollout and national network upgrade schedule.

---

### 9. Why This Case Demonstrates Senior BA Thinking
- **Avoids vanity metrics:** Focuses on churn and revenue durability rather than short-term acquisition volume.
- **Supports decision-making:** Each recommendation is tied to hypotheses, KPIs, and clear trade-offs.
- **Scales across industries:** The framework (classification → mapping → KPIs → hypotheses → recommendations) applies to any subscription or service business.
