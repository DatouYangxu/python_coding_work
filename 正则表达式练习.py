import re 
# def inform(html,name):
#     pattern='title="%s">%s</a>'%(name,name)
#     id=html.find(pattern)
#     html=html[id:]
#     pat1=r'<span\sclass="sy\wclass\wusers\wst\wnum"\stitle="\d+">(\d+)</a>'
#     xuehao=re.search(pat1,html)
#     pat2=r'<span\sclass="sum_score_tip">\.(\d+\.\d+)\.</span>'
#     fenshu=re.search(pat2,html,re.S)
#     return xuehao,fenshu
# html='''<a href="https://www.trustie.net/users/yangMJ" class="fl sy_class_users_st_name" target="_blank" title="杨铭金">杨铭金</a>
#         </td>
#         <td>
#           <span class="sy_class_users_st_num" title="1609037019">1609037019</span>
#         </td>
#         <td>
#               <a href="https://www.trustie.net/courses/888/show_member_score?member_id=31703" class="" data-remote="true">674.00</a>
#         </td>
#         <td>0</td>
#         <td>
#           <a href="https://www.trustie.net/courses/888/show_member_act_score?member_id=31703" class="" data-remote="true">2</a>
#         </td>
#         <td class="pr">
#           <span class="sum_score_tip">
#               676.00
#           </span>
# '''
# name='杨铭金'
# print(inform(html,name))

html='<tr class="row" data-row-key="123" style="color:red">单元格内容</tr>'
pattern=r'<tr'