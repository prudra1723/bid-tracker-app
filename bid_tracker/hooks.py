app_name = "bid_tracker"
app_title = "Bid Tracker"
app_publisher = "Rudra Pandey"
app_description = "Custom ERPNext module for pre-contract bid tracking"
app_email = "bidtrackererpnext@gmail.com"
app_license = "MIT"

after_install = "bid_tracker.install.after_install"

doctypes_js = {
    "Bid Record": "public/js/bid_record.js",
}
