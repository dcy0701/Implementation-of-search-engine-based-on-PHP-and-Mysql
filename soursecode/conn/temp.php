<?php
$so = scws_new();
$so->set_charset('gbk');
//$so->set_dict('C://Program Files//scws//etc//dict.utf8.xdb');
$so->set_rule('C://Program Files//scws//etc//rules.utf8.ini');
// 这里没有调用 set_dict 和 set_rule 系统会自动试调用 ini 中指定路径下的词典和规则文件
//$so->send_text("我是一个中国人,我会C++语言,我也有很多T恤衣服");
$str=$_GET["keyword"];
$str = iconv('utf-8','gb2312',$str);
echo $str;
$so->send_text($str);
$content="";
while ($tmp = $so->get_result())
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
$content1 = urlencode($content);
$content1 = str_replace("%","",$content1);
$content1 = str_replace("+"," ",$content1);
$count = substr_count($content1," ");
echo $count."????";
/*
if($count==2){
	$content1 = str_replace(" ","",$content1);
}
else{
	$content1=$content1;
}*/
#$content1.=" ";
session_start();//通过session传递数据
$_SESSION['keyword']=$content1;
echo $_SESSION['keyword'];
echo $content1;
$so->close();
$url = "query.php"; 


if (isset($url)) //页面重定向
{ 
Header("Location: $url"); 
} 
?>