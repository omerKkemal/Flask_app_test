import threading
from flask import Flask
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from kivy.clock import Clock
import webbrowser

# Conditional imports based on platform
if platform == "android":
    from jnius import autoclass
    from android.permissions import request_permissions, Permission

    WebView = autoclass("android.webkit.WebView")
    WebViewClient = autoclass("android.webkit.WebViewClient")
    PythonActivity = autoclass("org.kivy.android.PythonActivity")
    View = autoclass("android.view.View")
    Color = autoclass("android.graphics.Color")

# --- CSS Variables ---
CSS_STYLES = """
body {
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #6e8efb, #a777e3);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
    color: white;
}
.content {
    text-align: center;
    padding: 20px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
}
h1 {
    font-size: 2.5rem;
    margin-bottom: 20px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}
p {
    font-size: 1.2rem;
    margin-bottom: 15px;
}
.btn {
    display: inline-block;
    padding: 10px 20px;
    margin: 10px;
    background: rgba(255, 255, 255, 0.2);
    color: white;
    text-decoration: none;
    border-radius: 5px;
    transition: all 0.3s ease;
}
.btn:hover {
    background: rgba(255, 255, 255, 0.3);
    transform: translateY(-2px);
}
"""

# Template function
def render_html(title, content):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>{CSS_STYLES}</style>
        <title>{title}</title>
    </head>
    <body>
        <div class="content">
            {content}
        </div>
    </body>
    </html>
    """

# --- Flask server ---
flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    platform_name = "Android" if platform == "android" else "Desktop"
    content = f"""
        <h1>Hello from Flask inside Kivy 🚀</h1>
        <p>This content is served from a Flask web server</p>
        <p>Running on: {platform_name}</p>
        <div>
            <a href="/page1" class="btn">Page 1</a>
            <a href="/page2" class="btn">Page 2</a>
        </div>
    """
    return render_html("Home", content)

@flask_app.route('/page1')
def page1():
    content = """
        <h1>Page 1</h1>
        <p>This is the first page of our Flask app</p>
        <a href="/" class="btn">Back to Home</a>
    """
    return render_html("Page 1", content)

@flask_app.route('/page2')
def page2():
    content = """
        <h1>Page 2</h1>
        <p>This is the second page of our Flask app</p>
        <a href="/" class="btn">Back to Home</a>
    """
    return render_html("Page 2", content)

def start_flask():
    flask_app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)

# --- Kivy App ---
class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        if platform == "android":
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.INTERNET])
            Clock.schedule_once(self.start_android_webview, 3)
        else:
            from kivy.uix.button import Button
            from kivy.uix.label import Label
            
            self.add_widget(Label(text="Flask + Kivy Desktop Test", size_hint_y=0.2))
            
            btn_open = Button(text="Open in Browser", size_hint_y=0.2)
            btn_open.bind(on_press=self.open_in_browser)
            self.add_widget(btn_open)
            
            btn_info = Button(text="Server Information", size_hint_y=0.2)
            btn_info.bind(on_press=self.show_info)
            self.add_widget(btn_info)
            
            self.info_label = Label(text="Server running at http://127.0.0.1:5000", 
                                   size_hint_y=0.4)
            self.add_widget(self.info_label)

    def open_in_browser(self, instance):
        webbrowser.open('http://127.0.0.1:5000')

    def show_info(self, instance):
        self.info_label.text = "Flask server is running locally.\nYou can access it in your browser."

    def start_android_webview(self, dt):
        if platform == "android":
            try:
                activity = PythonActivity.mActivity
                webview = WebView(activity)
                settings = webview.getSettings()
                settings.setJavaScriptEnabled(True)
                settings.setDomStorageEnabled(True)
                
                # Fix for black screen
                webview.setLayerType(View.LAYER_TYPE_HARDWARE, None)
                webview.setBackgroundColor(Color.WHITE)
                
                webview_client = WebViewClient()
                webview.setWebViewClient(webview_client)
                
                webview.loadUrl("http://127.0.0.1:5000")
                activity.setContentView(webview)
                
            except Exception as e:
                from kivy.uix.label import Label
                self.add_widget(Label(text=f"WebView Error: {str(e)}"))

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    threading.Thread(target=start_flask, daemon=True).start()
    MyApp().run()