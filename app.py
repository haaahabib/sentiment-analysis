import streamlit as st
import tensorflow as tf
from transformers import BertTokenizer
from streamlit_lottie import st_lottie
import requests
import time

st.set_page_config(
    page_title="Airline Sentiment Analysis",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(""" 
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        
        .stApp {
            font-family: 'Poppins', sans-serif;
        }
        
        .sentiment-box {
            font-size: 1.2rem;
            font-weight: normal;
            padding: 0.8rem;
            border-radius: 8px;
            margin-top: 1rem;
            text-align: left;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        }
        
        .sentiment-box .result {
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }
        
        .sentiment-box .sentiment {
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        
        .sentiment-box .confidence {
            color: #888;
        }

        .positive {
            background: #e1f5e1;
            border-left: 4px solid #4caf50;
        }
        
        .negative {
            background: #fbe9e7;
            border-left: 4px solid #ff4d4d;
        }

        .history-item {
            font-size: 1rem;
            margin-bottom: 0.5rem;
            padding: 0.8rem;
            border-radius: 8px;
            background: #f9f9f9;
            box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.1);
        }

        .history-item .review {
            font-style: italic;
        }

        .history-item .sentiment {
            font-weight: bold;
            margin-top: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_lottie_animation(url):
    try:
        response = requests.get(url)
        return response.json()
    except:
        return None

plane_animation = load_lottie_animation("https://assets4.lottiefiles.com/packages/lf20_jbrw3hcz.json")
loading_animation = load_lottie_animation("https://assets9.lottiefiles.com/packages/lf20_p8bfn5to.json")
customer_service_animation = load_lottie_animation("https://assets6.lottiefiles.com/packages/lf20_ucbyrun5.json")

@st.cache_resource
def load_model():
    model_path = r'C:\Users\user\Documents\webdeploy\reviews\BERT_Model'
    model = tf.saved_model.load(model_path)
    return model

@st.cache_resource
def load_tokenizer():
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    return tokenizer

model = load_model()
tokenizer = load_tokenizer()

sentiment_map = {0: 'Negative', 1: 'Positive'}

def predict_sentiment(text):
    tokens = tokenizer(
        text,
        max_length=128,
        truncation=True,
        padding='max_length',
        return_tensors='tf'
    )
    inputs = {
        'input_ids': tokens['input_ids'],
        'attention_mask': tokens['attention_mask'],
        'token_type_ids': tf.zeros_like(tokens['input_ids'])
    }
    result = model.signatures['serving_default'](**inputs)
    logits = result['logits'].numpy()
    predicted_class = tf.argmax(logits, axis=1).numpy()[0]
    confidence = tf.nn.softmax(logits, axis=1).numpy()[0][predicted_class]
    return sentiment_map[predicted_class], confidence

# History
if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_history(review, sentiment, confidence):
    st.session_state.history.append({
        'Review': review,
        'Sentiment': sentiment,
        'Confidence': confidence
    })

# Predict result
def result_box(sentiment, confidence, user_input):
    sentiment_class = "positive" if sentiment == "Positive" else "negative"
    return f"""
    <div class='sentiment-box {sentiment_class}'>
        <p class='result'>{sentiment} - {confidence:.2%}</p>
        <p class='review'>" {user_input} "</p>
    </div>
    """

def main():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if plane_animation:
            st_lottie(plane_animation, height=200, key="plane")

    st.markdown(
        "<h2 style='text-align: center;'>📝 Share Your Airline Experience</h2>",
        unsafe_allow_html=True
    )

    user_input = st.text_area(
        "Share your experience with Singapore Airlines",
        height=150,
        placeholder="Example: Singapore Airlines was comfortable and the crew was very professional..."
    )

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        analyze_button = st.button("⏳ Analyze Sentiment")
    
    if analyze_button and user_input.strip():
        with st.spinner("Analyzing your review..."):
            if loading_animation:
                st_lottie(loading_animation, height=100, key="loading")
            time.sleep(1)
            
            sentiment, confidence = predict_sentiment(user_input)
            
            # Add to history
            add_to_history(user_input, sentiment, confidence)
            
            # Result box prediction
            st.markdown(result_box(sentiment, confidence, user_input), unsafe_allow_html=True)

    # History
    if st.session_state.history:
        st.markdown("")
        st.markdown("<h3 style='text-align: left;'>History of Reviews</h3>", unsafe_allow_html=True)
        for idx, record in enumerate(reversed(st.session_state.history), 1):
            st.markdown(f"""
            <div class='history-item'>
                <p class='review'>" {record['Review']} "</p>
                <p class='sentiment'>{record['Sentiment']} - {record['Confidence']:.2%}</p>
            </div>
            """, unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        if customer_service_animation:
            st_lottie(customer_service_animation, height=200, key="customer_service")
        
        st.markdown("---")
        st.markdown(""" 
        ### Developer Info
        👨‍💻 **Muhammad Habibulloh**  
        🎓 **20211037031159**   
        """)
        
        st.markdown("---")
        with st.expander("📝 Sample Reviews"):
            st.markdown(""" 
            **Positive Examples:**
            - "The flight crew was exceptional and made the journey comfortable."
            - "On-time departure and smooth landing. Great experience!"
            
            **Negative Examples:**
            - "Flight was delayed by 3 hours with no proper explanation."
            - "The seats were uncomfortable and the food was cold."
            """)

if __name__ == "__main__":
    main()
