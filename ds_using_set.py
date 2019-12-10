bri = set(['brazil', 'russia', 'india'])
if 'india' in bri:
    print('ths set is', bri) # 按照字符串长度自动排序

print( 'india' in bri)
print( 'china' in bri)

bric = bri.copy()
bric.add('usa')
print('ths new_set is', bric)
print( bric.issuperset(bri))

bri.remove('russia')
print(bri&bric ) #与操作取交集

