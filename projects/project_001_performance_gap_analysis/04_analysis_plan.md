# 04 Analysis Plan

## Analysis Objectives (Aligned to Hypotheses)
- H1 Process inefficiency: quantify cycle-time bottlenecks by stage, team, and project type.
- H2 Skill gaps: assess relationship between skill coverage/training completion and delivery quality or rework.
- H3 Workload imbalance: evaluate capacity utilization vs. delivery outcomes by team and time period.
- H4 Tooling issues: test whether system incidents or workflow disruptions correlate with delays.

## Key KPIs and Metrics
- Productivity: output per FTE, billable utilization %, hours per deliverable.
- Delivery: on-time delivery rate, schedule variance (planned vs actual), cycle time by stage.
- Quality: defect rate, rework hours %, escalation rate, CSAT.
- Resource balance: allocation variance, workload variance by team, queue length.
- Financials: margin %, cost overrun %, revenue leakage from delays.

## Analysis Techniques and Steps
1. Baseline trend analysis
   - Technique: time-series trends for productivity, on-time delivery, and cycle times.
   - Tools: SQL (data prep), Power BI (trend visuals).
   - Output: line charts by month, summary tables.

2. Variance analysis vs. plan
   - Technique: planned vs actual variance by project, team, and period.
   - Tools: SQL (variance calc), Excel (variance pivots).
   - Output: variance tables, heatmaps.

3. Cohort analysis by project start period
   - Technique: cohort performance for delivery timelines and quality.
   - Tools: SQL (cohort build), Power BI (cohort visuals).
   - Output: cohort tables, waterfall charts.

4. Skill gap impact assessment
   - Technique: correlation between skill coverage/training completion and rework/defects.
   - Tools: R (correlation/stat tests), Excel (summary).
   - Output: correlation matrix, scatter plots.

5. Workload imbalance analysis
   - Technique: capacity vs. demand by team; identify over-allocated periods.
   - Tools: SQL (capacity aggregation), Power BI (capacity dashboards).
   - Output: utilization dashboards, allocation variance charts.

6. Tooling disruption impact
   - Technique: correlate system outage/ticket spikes with delivery delays.
   - Tools: SQL (join incidents to schedules), R (correlation).
   - Output: incident vs delay plots, correlation tables.

## Expected Outputs
- Executive summary dashboard (Power BI) with KPIs and trends.
- Root-cause analysis tables by hypothesis (Excel/SQL output).
- Visuals: trend lines, cohort heatmaps, variance charts, correlation plots.
- Appendix dataset extracts for stakeholder review.
