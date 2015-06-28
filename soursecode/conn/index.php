<?php
    set_time_limit(0);
	$so = scws_new();
	$so->set_charset('gbk');
	$conn = mysql_connect("localhost","root","dcy0701") or die("数据库连接失败！".mysql_error());
	mysql_select_db("weibo",$conn);
	mysql_query("set names gbk");
	echo $conn;
	echo "数据库选择成功";
	//include_once("conn/conn.php");
	$result = mysql_query("select * from think_test",$conn);
	$glo = 0;
while($myrow=mysql_fetch_array($result)){
	$content_tr = $myrow[4];
	$sourse_tr = $myrow[11];
	$name_tr = $myrow['name'];
	$conname = "";
	$content = "";
	$consou = "";
	//echo $content_tr;
	$so->send_text($content_tr);
	while($tmp = $so->get_result())
		{
		//print_r($tmp);
		$cou = count($tmp);
		//echo $cou;
		//echo $tmp[0]['word'];
		for($a=0;$a<$cou;$a+=1){
		$content = $content.$tmp[$a]['word']." ";
		}
		//print_r($tmp);
		echo "<p>";
		//print $content;
	}
	print $content;
	$so->send_text($name_tr);
	//echo "sb";
	//echo $conname;
	while($tmp1 = $so->get_result())
		{
		//print_r($tmp1);
		$cou1 = count($tmp1);
		//echo $cou1;
		//echo $tmp[0]['word'];
		for($a=0;$a<$cou1;$a+=1){
		$conname = $conname.$tmp1[$a]['word']." ";
		}
		//print_r($tmp);
		echo "<p>";
		//print $conname;
	}
	print $conname;
	$so->send_text($sourse_tr);
	while($tmp2 = $so->get_result())
		{
		//print_r($tmp2);
		$cou2 = count($tmp2);
		//echo $cou2;
		//echo $tmp[0]['word'];
		for($a=0;$a<$cou2;$a+=1){
		$consou = $consou.$tmp2[$a]['word']." ";
		}
		//print_r($tmp);
		echo "<p>";
	}
	print $consou;
	$content1 = urlencode($content);
	$consou1 = urlencode($consou);
	$conname1 = urlencode($conname);

	$content1 = str_replace("%","",$content1);
	$content1 = str_replace("+"," ",$content1);
	$consou1 = str_replace("%","",$consou1);
	$consou1 = str_replace("+"," ",$consou1);
	$conname1 = str_replace("%","",$conname1);
	$conname1 = str_replace("+"," ",$conname1);
	echo $conname1."哈哈";
	echo $content1;
	echo $consou1;

	$sqlstr1="insert into think_love values('".$glo."','".$myrow[1]."','".$myrow[2]."','".$myrow[3]."','".$myrow[4]."','".$content1."','".$myrow[6]."','".$myrow[7]."','".$myrow[8]."','".$myrow[9]."','".$myrow[10]."','".$myrow[11]."','".$myrow[12]."','".$myrow[13]."','".$conname1."','".$consou1."')";
	$glo += 1;
	$result1 = mysql_query($sqlstr1,$conn);
	if($result1){
		echo "添加成功";

	}else{
		echo "添加失败";
	}
}
