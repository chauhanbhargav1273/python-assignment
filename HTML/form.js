function checkfname()
		{
			var f = document.frm.fname.value;
			var reg=/^[A-Za-z]+$/;
			if(f=="")
			{
				document.getElementById("fname").innerHTML="Please Enter First Name"
			}
			else if(!reg.test(f))
			{
				document.getElementById("fname").innerHTML="Please Enter Only Alphabets";
			}
			else
			{
				document.getElementById("fname").innerHTML=""
			}
		}
		function checklname()
		{
			var f= document.frm.lname.value;
			var reg=/^[A-Za-z]+$/;
			if(f=="")
			{
				document.getElementById("lname").innerHTML="Please enter last name"
			}
			else if(!reg.test(f))
			{
				document.getElementById("lname").innerHTML="please enter only Alphabets"
			}
			else
			{
				document.getElementById("lname").innerHTML=""
			}
		}
		function checkemail()
		{
			var f= document.frm.email.value;
			var reg=/^[A-Za-z0-9-_.]+@[A-Za-z]+\.[A-Za-z]{2,4}$/;
			if(f=="")
			{
				document.getElementById("email").innerHTML="Please enter email"
			}
			else if(!reg.test(f))
			{
				document.getElementById("email").innerHTML="Please Enter Valid Email"
			}
			else
			{
				document.getElementById("email").innerHTML=""
			}
		}
		function checkmobile()
		{
			var f= document.frm.mobile.value;
			var reg=/^\d{10}$/;
			if(f=="")
			{
				document.getElementById("mobile").innerHTML="Please Enter Mobile";
			}
			else if(!reg.test(f))
			{
				document.getElementById("mobile").innerHTML="Please Enter 10 Digits Only";
			}
			else
			{
				document.getElementById("mobile").innerHTML="";	
			}
		}
		function checkPassword()
		{
			var f=document.frm.password.value;
			var reg=/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;
			if(f=="")
			{
				document.getElementById("password").innerHTML="Please Enter Password";
			}
			else if(!reg.test(f))
			{
				document.getElementById("password").innerHTML="Min 1 Digit, Upper,Lower & Special(8,15)";
			}
			else
			{
				document.getElementById("password").innerHTML="";	
			}

		}
		function cPassword()
		{
			var f=document.frm.password.value;
			var g=document.frm.cpassword.value;
			if(g=="")
			{
				document.getElementById("cpassword").innerHTML="Please Enter Confirm Password";	
			}
			else if(f!=g)
			{
				document.getElementById("cpassword").innerHTML="Password and confirm Password Does Not Match";
			}
			else
			{
				document.getElementById("cpassword").innerHTML="";	
			}
			
		}