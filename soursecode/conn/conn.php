<?php
$conn = mysql_connect("localhost","root","dcy0701") or die("���ݿ�����ʧ�ܣ�".mysql_error());
mysql_select_db("weibo",$conn);
mysql_query("set names utf8");
echo $conn;
echo "���ݿ�ѡ��ɹ�";
?>