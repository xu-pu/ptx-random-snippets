/*======================================================
  师大教务系统评课脚本
========================================================
  使用方法：将下面代码拷入浏览器的consloe
  注意：选项为第一个良好，其余全优秀，可以直接按提交
========================================================*/ 

doc = document.getElementById('iframeautoheight').contentWindow.document
select_list = doc.getElementById('DataGrid1').getElementsByTagName('select')
for (var i = 0; i < select_list.length; i++) {
    select_list[i].selectedIndex = 1
}
select_list[0].selectedIndex = 2
