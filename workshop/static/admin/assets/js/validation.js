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
    first_name = $("#frmProfileEdit").find('[name="first_name"]').val();
    last_name = $("#frmProfileEdit").find('[name="last_name"]').val();
    username = $("#frmProfileEdit").find('[name="username"]').val();
    email = $("#frmProfileEdit").find('[name="email"]').val();
    phone_number = $("#frmProfileEdit").find('[name="phone_number"]').val();
    if (!first_name) {
        alert("First Name required");
        return false
    }
    if (!last_name) {
        alert("Last Name required");
        return false
    }
    if (!username) {
        alert("Username required");
        return false
    }
    if (!email) {
        alert("Email required");
        return false
    }
    if (!phone_number) {
        alert("Phone Number required");
        return false
    }
    return true;
}

function validateForm5() {
    password = $("#frmChangPwd").find('[name="password"]').val();
    confirm_password = $("#frmChangPwd").find('[name="confirm_password"]').val();
    if (password != confirm_password) {
        alert("Password and Confirm Password should be same");
        return false
    }
    return true;
}

function validateForm6() {
    spare_part_id = $("#frmJobSP").find('[name="spare_part_id"]').val();
    qty = $("#frmJobSP").find('[name="qty"]').val();
    cost_per_unit = $("#frmJobSP").find('[name="cost_per_unit"]').val();
    if (!spare_part_id) {
        alert("Select Sparepart");
        return false
    }
    if (!qty || qty <= 0) {
        alert("Enter Qty");
        return false
    }
    if (!cost_per_unit || cost_per_unit <= 0) {
        alert("Enter Cost / Unit");
        return false
    }
    return true;
}

function validateForm7() {
    sparepart = $("#frmSP").find('[name="spare_part_name"]').val();
    qty = $("#frmSP").find('[name="cost_per_unit"]').val();
    if (!sparepart) {
        alert("Enter Sparepart");
        return false
    }
    if (!cost_per_unit || cost_per_unit <= 0) {
        alert("Enter Cost / Unit");
        return false
    }
    return true;
}

function validateForm8() {
    description = $("#frmJobService").find('[name="description"]').val();
    fee = $("#frmJobService").find('[name="fee"]').val();
    if (!description) {
        alert("Enter Description");
        return false
    }
    if (!fee || fee <= 0) {
        alert("Enter Fee");
        return false
    }
    return true;
}