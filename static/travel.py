from js import my_alert

all_1 = Element('all_1')
all_2 = Element('all_2')

nav_tab_a = Element('nav_tab_a')
nav_tab_b = Element('nav_tab_b')
nav_tab_c = Element('nav_tab_c')

title_a = Element('title_a')
input_int_a = Element('input_int_a')
output_a = Element('output_a')
diamond_a = Element('diamond_a')
table_a = Element('table_a')
diamond_a_per_num = 40
material_a = [0.135, 0.2, 0.3, 0.365]
table_a.element.rows[2].cells[1].innerHTML = "0.001"
table_a.element.rows[3].cells[1].innerHTML = "0.05"
table_a.element.rows[4].cells[1].innerHTML = "0.15"
table_a.element.rows[5].cells[1].innerHTML = "0.2"
table_a.element.rows[6].cells[1].innerHTML = "0.599"

title_b = Element('title_b')
input_int_b = Element('input_int_b')
output_b = Element('output_b')
diamond_b = Element('diamond_b')
table_b = Element('table_b')
diamond_b_per_num = 20
material_b = []
table_b.element.rows[2].cells[1].innerHTML = "0.0"
table_b.element.rows[3].cells[1].innerHTML = "0.0065"
table_b.element.rows[4].cells[1].innerHTML = "0.13"

title_a.element.innerHTML = '角色機率試算 (1抽={}鑽)'.format(diamond_a_per_num)
title_b.element.innerHTML = '道具機率試算 (1抽={}鑽)'.format(diamond_b_per_num)

def calculate_a():
  if input_int_a.element.value:
    if input_int_a.element.value.isnumeric():
      if int(input_int_a.element.value) >= 1 and int(input_int_a.element.value) <= 10000:
        # output_a.write(input_int_a.element.value)
        diamond_a.write(str(int(input_int_a.element.value)*diamond_a_per_num))

        # try:
        #   my_alert(table_a.element.rows[0].cells.length)
        # except Exception as e:
        #   my_alert(e)

        tmp_str = '{:.2f}'.format(float(table_a.element.rows[2].cells[1].innerHTML) * int(input_int_a.element.value))
        table_a.element.rows[2].cells[2].innerHTML = tmp_str
        tmp_str = '{:.2f}'.format(float(table_a.element.rows[3].cells[1].innerHTML) * int(input_int_a.element.value))
        table_a.element.rows[3].cells[2].innerHTML = tmp_str
        tmp_str = '{:.2f}'.format(float(table_a.element.rows[4].cells[1].innerHTML) * int(input_int_a.element.value))
        table_a.element.rows[4].cells[2].innerHTML = tmp_str
        tmp_str = '{:.2f}'.format(float(table_a.element.rows[5].cells[1].innerHTML) * int(input_int_a.element.value))
        table_a.element.rows[5].cells[2].innerHTML = tmp_str
        tmp_str = '{:.2f}'.format(float(table_a.element.rows[6].cells[1].innerHTML) * int(input_int_a.element.value))
        table_a.element.rows[6].cells[2].innerHTML = tmp_str

        tmp_str = '{:.2f}'.format(float(table_a.element.rows[2].cells[2].innerHTML) + (float(table_a.element.rows[6].cells[2].innerHTML)/5) * material_a[0])
        table_a.element.rows[2].cells[3].innerHTML = tmp_str
        tmp_str = '{:.2f}'.format(float(table_a.element.rows[3].cells[2].innerHTML) + (float(table_a.element.rows[6].cells[2].innerHTML)/5) * material_a[1])
        table_a.element.rows[3].cells[3].innerHTML = tmp_str
        tmp_str = '{:.2f}'.format(float(table_a.element.rows[4].cells[2].innerHTML) + (float(table_a.element.rows[6].cells[2].innerHTML)/5) * material_a[2])
        table_a.element.rows[4].cells[3].innerHTML = tmp_str
        tmp_str = '{:.2f}'.format(float(table_a.element.rows[5].cells[2].innerHTML) + (float(table_a.element.rows[6].cells[2].innerHTML)/5) * material_a[3])
        table_a.element.rows[5].cells[3].innerHTML = tmp_str
      else:
        my_alert('請輸入1~10000之間的整數')
    else:
      my_alert('請輸入1~10000之間的整數')
  else:
    my_alert('請輸入1~10000之間的整數')


def calculate_b():
  if input_int_b.element.value:
    if input_int_b.element.value.isnumeric():
      if int(input_int_b.element.value) >= 1 and int(input_int_b.element.value) <= 10000:
        # output_b.write(input_int_b.element.value)
        diamond_b.write(str(int(input_int_b.element.value)*diamond_b_per_num))

        tmp_str = '{:.2f}'.format(float(table_b.element.rows[2].cells[1].innerHTML) * int(input_int_b.element.value))
        table_b.element.rows[2].cells[2].innerHTML = tmp_str
        tmp_str = '{:.2f}'.format(float(table_b.element.rows[3].cells[1].innerHTML) * int(input_int_b.element.value))
        table_b.element.rows[3].cells[2].innerHTML = tmp_str
        tmp_str = '{:.2f}'.format(float(table_b.element.rows[4].cells[1].innerHTML) * int(input_int_b.element.value))
        table_b.element.rows[4].cells[2].innerHTML = tmp_str

        tmp_str = '{:.2f}'.format(float(table_b.element.rows[3].cells[2].innerHTML)/5.0 + float(table_b.element.rows[4].cells[2].innerHTML)/25.0)
        table_b.element.rows[2].cells[3].innerHTML = tmp_str

      else:
        my_alert('請輸入1~10000之間的整數')
    else:
      my_alert('請輸入1~10000之間的整數')
  else:
    my_alert('請輸入1~10000之間的整數')

  
def tab_a():
  if nav_tab_a.element.className == 'nav-link':
    nav_tab_a.element.setAttribute('class', 'nav-link active')
    nav_tab_b.element.setAttribute('class', 'nav-link')
    # nav_tab_c.element.setAttribute('class', 'nav-link')
    all_1.element.style.display = 'block'
    all_2.element.style.display = 'none'

def tab_b():
  if nav_tab_b.element.className == 'nav-link':
    nav_tab_b.element.setAttribute('class', 'nav-link active')
    nav_tab_a.element.setAttribute('class', 'nav-link')
    # nav_tab_c.element.setAttribute('class', 'nav-link')
    all_1.element.style.display = 'none'
    all_2.element.style.display = 'block'

def test():
  print('JHI')