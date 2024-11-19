css = '''
<style>


.chat-container {
        height: calc(100vh - 150px);
        overflow-y: auto;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
}

.chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
}

.chat-message.bot {
        background-color: #475063;
}

.chat-message.user {
        background-color: #2c3e50;
}


.chat-message .avatar {
        max-width: 70px;
        max-height: 70px;
        border-radius: 50%;
        object-fit: cover;
        margin-right: 1rem;
}

.chat-message .message {
        width: 85%;
        padding: 0 1.5rem;
        color: #fff;
        word-wrap: break-word;
}

.stTextInput {
    position: fixed;
    bottom: 1rem;
}

</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://images.pexels.com/photos/8566531/pexels-photo-8566531.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" alt="Bot Avatar" />
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" alt="User Avatar" />
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
