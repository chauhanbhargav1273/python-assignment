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
