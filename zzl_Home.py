"""
工作室名字：星辰叙事者
根据地用户：分享后所有人可见
根据地用途：游戏分享、数据收集、兴趣推荐、经历分享、查找攻略、个人经历
最喜欢的现有模块：兴趣推荐、攻略区、留言区、讨论区、
现有模块改进灵感：加入ai系统
原创模块：及时攻略
原创模块一句话功能介绍：将玩家输入特定的游戏与游戏进度，跳出攻略
"""
import streamlit as st
from PIL import Image
import time

page = st.sidebar.radio('首页',['讨论区', 'UP主', '攻略区', '兴趣推荐', '其他'])
def page1():
    st.write('我的留言区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🦼'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🦼'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
            
    
    
    
    
def page2():
    pass

def page3():
    with open('骄傲的少年.mp3','rb') as f:
        mymp3 =f.read()
    st.audio(mymp3,format='audio/mp3',start_time = 0)
    
    st.image('OIP-C.jpg')
    st.write('-------------------------')
    st.write('星际玩家不要视力')

def page4():
    '词典'
    st.write(':motorized_wheelchair:词典:motorized_wheelchair:')
    with open('words_space.txt','r', encoding='utf-8') as f:
        word_list=f.read().split('\n')
    for i in range(len(word_list)):
        word_list[i]=word_list[i].split('#')
    word_dict={}
    for i in word_list:
        word_dict[i[1]]=[int(i[0]),i[2]]#单词：[计数，中文]
        
    with open('check_out_times.txt', 'r',encoding= 'utf-8') as f:
        time_list = f.read().split('\n')
    for i in range(len(time_list)):
        time_list[i]=time_list[i].split('#')

    time_dict={}
    for i in time_list:
        time_dict[int(i[0])]=int(i[1])
    
    word = st.text_input('请输入单词：')
    if word in word_dict:
        st.write(word_dict[word])
        n = word_dict[word][0]
        if n in time_dict:
            time_dict[n] += 1
        else:
            time_dict[n]=1
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message=''
            for k,v in time_dict.items():
                message += str(k)+'#'+str(v)+'\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数:',time_dict[n])
        
            
        
        if word=='python':
            st.code('''触发了一个彩蛋，这是一行python代码……
                    print("halo world")''')
        if word=='arknight':
            st.code('''原来，你也玩舟？！''')
            st.balloons()
        if word=='snow'or word=='winter':
            st.snow()
        if word=='title':
            st.table('ZZL')
        if word =='error':
            st.error('报错！')
        if word=='information':
            st.info('修改后的图片，可以鼠标右击选择【另存为】')
        if word=='wait':
            with st.spinner('Waiting。。。'):
                time.sleep(3)
            st.success('恭喜你成功啦！')
    
def page5():
    st.write(':motorized_wheelchair:图片处理工具:motorized_wheelchair:')
    uploaded_file=st.file_uploader('上传图片',type=['png','jpg','jpeg'])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        tab1,tab2,tab3,tab4 = st.tabs(['原图','图一','图二','图三'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 1))
        with tab4:
            st.image(img_change(img, 1, 0, 1))
        
def img_change(img,rc,gc,bc):
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img
            
    
if page =='讨论区':
    page1()
elif page =='UP主':
    page2()
elif page =='攻略区':
    page3()
elif page =='兴趣推荐':
    page4()
elif page =='其他':
    page5()