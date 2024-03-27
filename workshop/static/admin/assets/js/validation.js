$(function () {
    "use strict"
    //
})

function validateForm1() {
    sparepart = $("#frmBuySparePart").find('[name="spare_part_id"]').val();
    qty = $("#frmBuySparePart").find('[name="qty"]').val();
    if (!sparepart) {
        alert("Select Sparepart");
        return false
    }
    if (!qty || qty <= 0) {
        alert("Enter Qty");
        return false
    }
    return true;
}

function validateForm2() {
    from_date = $("#frmSearch").find('[name="from_date"]').val();
    to_date = $("#frmSearch").find('[name="to_date"]').val();
    if (!from_date) {
        alert("Select From Date");
        return false
    }
    if (!to_date) {
        alert("Select To Date");
        return false
    }
    return true;
}

function validateForm3() {
    brand_name = $("#frmJob").find('[name="brand_name"]').val();
    model_name = $("#frmJob").find('[name="model_name"]').val();
    make_year = $("#frmJob").find('[name="make_year"]').val();
    color = $("#frmJob").find('[name="color"]').val();
    job_description = $("#frmJob").find('[name="job_description"]').val();
    if (!brand_name) {
        alert("Brand Name required");
        return false
    }
    if (!model_name) {
        alert("Model Name required");
        return false
    }
    if (!make_year) {
        alert("Make Year required");
        return false
    }
    if (!color) {
        alert("Color required");
        return false
    }
    if (!job_description) {
        alert("Job Description required");
        return false
    }
    return true;
}

function validateForm4() {

}

function validateForm5() {

}