# 03 Data Inventory

## Data Sources
- Dataset: Project delivery milestones and schedules
  - Source system: Jira + Smartsheet (Project Management Tools)
  - Owner / stakeholder: PMO Director
  - Time granularity: Weekly
  - Data quality risks: Inconsistent status updates; manual entry delays
  - Access constraints or dependencies: Requires PMO approval; limited historical exports
- Dataset: Time tracking and utilization
  - Source system: UKG Pro (HRMS/Timekeeping)
  - Owner / stakeholder: HR Operations
  - Time granularity: Daily
  - Data quality risks: Missing time entries; non-standard codes
  - Access constraints or dependencies: HR data privacy approvals; role-based access
- Dataset: Resource allocation and staffing plans
  - Source system: Resource Management by Smartsheet
  - Owner / stakeholder: Resource Manager
  - Time granularity: Weekly
  - Data quality risks: Allocation not updated for urgent reassignments
  - Access constraints or dependencies: Dependent on PMO schedule alignment
- Dataset: Skills matrix and certifications
  - Source system: Cornerstone OnDemand (LMS)
  - Owner / stakeholder: Learning & Development Lead
  - Time granularity: Monthly
  - Data quality risks: Outdated profiles; incomplete assessments
  - Access constraints or dependencies: Requires L&D export and consent for assessment data
- Dataset: Onboarding and training completion
  - Source system: Workday Learning (LMS)
  - Owner / stakeholder: HR Business Partner
  - Time granularity: Monthly
  - Data quality risks: Training logged but not completed; manual overrides
  - Access constraints or dependencies: HR approval; data joins to employee IDs
- Dataset: Delivery quality and rework
  - Source system: ServiceNow (ticketing/defects)
  - Owner / stakeholder: QA Manager
  - Time granularity: Weekly
  - Data quality risks: Defects misclassified; rework not consistently linked to projects
  - Access constraints or dependencies: Requires QA reporting access; project ID mapping
- Dataset: Client escalations and satisfaction
  - Source system: Salesforce Service Cloud (CRM)
  - Owner / stakeholder: Customer Success Lead
  - Time granularity: Monthly
  - Data quality risks: Escalations logged inconsistently; survey response bias
  - Access constraints or dependencies: Customer data access controls; opt-in survey data
- Dataset: Financial performance by project
  - Source system: NetSuite (Finance/ERP)
  - Owner / stakeholder: Finance Controller
  - Time granularity: Monthly
  - Data quality risks: Cost allocations lag actuals; revenue recognition timing
  - Access constraints or dependencies: Finance approval; restricted margin fields
- Dataset: Change requests and scope adjustments
  - Source system: Jira + SharePoint (Change control logs)
  - Owner / stakeholder: PMO Change Manager
  - Time granularity: Weekly
  - Data quality risks: Change requests not logged for smaller scope shifts
  - Access constraints or dependencies: Requires PMO approval; shared folder permissions
- Dataset: Workflow cycle times by stage
  - Source system: Power BI data mart (aggregated from Jira)
  - Owner / stakeholder: BI Manager
  - Time granularity: Weekly
  - Data quality risks: Stage definitions differ by team; ETL refresh delays
  - Access constraints or dependencies: Dependent on BI team refresh cadence

## Data Ownership and Access

## Data Dictionary (Draft)

## Data Refresh Cadence

## Known Limitations
