<!doctype html>
<html lang="en">
 <head>
  <meta charset="utf-8">
  <meta name="Generator" content="EditPlus®">
  <link rel="shortcut icon" href="icon_1.png">
  <title>结果</title>
 </head>
<body bgcolor="#e7e7e7" text="red" background="id/0.jpg"> 
hi，这是您的搜索结果<?php 
#echo $_GET["keyword"]
$so = scws_new();
$so->set_charset('utf-8');
$conn = mysql_connect("localhost","root","dcy0701") or die("数据库连接失败！".mysql_error());
mysql_select_db("weibo",$conn);
mysql_query("set names utf8");

if (1==1){
	#echo "您输入的是关键词";
	//$keyword = $_GET["keyword"];
	session_start();
	/*
	$keyword = $_SESSION['keyword'];
	//$keyword = iconv('utf-8','gb2312',$str);
	$so->send_text($keyword);
	$content="";
	echo $keyword;
	while($tmp = $so->get_result())
		{
		print_r($tmp);
		$cou = count($tmp);
		echo $cou;
		print_r($tmp);
		for($a=0;$a<$cou;$a+=1){
		$content = $content.$tmp[$a]['word']." ";
		}
		echo "<p>";
		}
	echo $content;
	echo "?????????";
	$content1 = urlencode(iconv('UTF-8', 'GB2312', $content));
	$content1 = str_replace("%","",$content1);
	$content1 = str_replace("+"," ",$content1);
	echo "<p>";
	*/
	$content1 = $_SESSION['keyword'];
	#echo $content1;

	//echo urlencode(mb_convert_encoding($content1, 'gbk', 'utf-8'))." ";
	//echo urlencode(iconv('UTF-8', 'GB2312', '喜欢'));

	$sqlstr1="select * from final WHERE MATCH(content_tr) AGAINST('".$content1."')";
	#print $sqlstr1;
	$result=mysql_query($sqlstr1,$conn);
	#echo $result;
	#echo "here!!!!!!!!!!!!!";
	$num_page = 1;
	while($myrow=mysql_fetch_array($result)){
		//echo $myrow[0];
		echo "<p>";
		$temp_id = $myrow[0];
		$sqlstr2="select * from think_love where id = ".$temp_id;
		$result1=mysql_query($sqlstr2,$conn);
		//echo $result1;
		echo "<br/>";
		$love_content = mysql_fetch_array($result1);
		echo "第".$num_page."条:&nbsp;&nbsp;";
		$num_page+=1;
		echo $love_content[4];
		echo $love_content[11];
		$page = $love_content[0]+1;
		echo "<a href =id/".$page.".html> 详细地址</a>";
		echo "<br/>";
	}


	}
	else
		{
	print "您输入的是关键词和用户名";
}
?>
</form> 
</body> 
</html> 