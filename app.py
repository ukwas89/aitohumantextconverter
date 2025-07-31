import streamlit as st

# Page config
st.set_page_config(
    page_title="AI to Human Text Converter – Free",
    layout="centered",
    initial_sidebar_state="auto"
)

# Custom CSS styling
st.markdown("""
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .main {
            background: linear-gradient(135deg, #0ea5e9, #3b82f6);
            color: #fff;
        }
        .container {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 12px 28px rgba(0, 0, 0, 0.1);
        }
        h1 {
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(90deg, #3b82f6, #0ea5e9);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .cta {
            background-color: #B3E4FF;
            padding: 0.75rem 1.5rem;
            color: white;
            font-weight: 600;
            border-radius: 8px;
            text-decoration: none;
        }
        .cta:hover {
            background-color: #0284c7;
        }
        a {
            color: #3b82f6;
            text-decoration: none;
            font-weight: 600;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# App content


st.markdown("<h1>AI to Human Text Converter</h1>", unsafe_allow_html=True)
st.write("Make your AI content sound natural, human, and undetectable — completely free.")

st.markdown(
    '<a class="cta" href="https://aitohumantextconverterfree.net/" target="_blank">Use this Free Ai text to human text converter</a>',
    unsafe_allow_html=True,
)

st.markdown("## What Is It?")
st.write("""
The [AI to Human Text Converter Free](https://aitohumantextconverterfree.net/) helps turn robotic or AI-written content into text that sounds natural, clear, and convincingly human.
It's fast, secure, and works with content generators like ChatGPT, Jasper, or Bard.
""")

st.markdown("## Key Features")
st.markdown("""
- 100% Free – no account or login required  
- Unlimited conversions  
- Bypasses AI detection tools easily  
- Fast and accurate results  
- Supports multiple languages  
- Perfect for SEO, blogs, schoolwork, and emails  
""")
st.write('Try it now and [humanize AI text](https://aitohumantextconverterfree.net/) in one click.')

st.markdown("## How It Works")
st.markdown("""
1. Paste your AI-generated content  
2. Click “Convert”  
3. Get rewritten text that sounds fully human  
""")
st.write("Use this [free AI humanizer](https://aitohumantextconverterfree.net/) daily with no limits.")

st.markdown("## Use Cases")
st.write("""
Whether you're a content creator, student, digital marketer, or freelancer, the
[AI to Human Text Converter](https://aitohumantextconverterfree.net/) gives you clean,
detection-safe results — perfect for publishing anywhere without rewriting manually.
""")

st.markdown("## Try It Now")

input_text = st.text_area("Paste your AI-generated text below:", height=200)

if st.button("Convert to Human Text"):
    # Placeholder for your converter logic
    if input_text.strip() == "":
        st.warning("Please enter some text to convert.")
    else:
        # You can replace this with your actual humanizing function
        humanized_text = input_text.replace("AI", "Human").replace("automated", "natural")
        st.success("Conversion successful!")
        st.text_area("Humanized Output", humanized_text, height=200)

st.markdown("----")
st.markdown(
    '<p style="text-align:center;font-size:0.9rem;color:#6b7280;">&copy; 2025 AI to Human Text Converter Free. <a href="https://aitohumantextconverterfree.net/" target="_blank">Visit the official site</a></p>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)
