from setuptools import setup, find_packages

setup(
    name='NetHyTech-STT',
    version='0.1',
    author='Anubhav Chaturvedi',
    author_email='chaturvedianubhav520@example.com',
    description='NetHyTech-STT: Convert Speech to Text with Ease!',
    long_description='''NetHyTech-STT is your go-to solution for converting speech to text effortlessly using Python. 
                        Whether you're transcribing audio files, building voice-enabled chatbots, or creating automatic 
                        transcriptions for videos and podcasts, NetHyTech-STT has you covered.

                        Key Features:
                        - Seamless integration with Selenium and the webdriver_manager
                        - Supports Python 3.8 and above
                        - Easy-to-use interface for live speech-to-text conversion
                        - Works with various web-based speech recognition APIs
                        
                        Use Cases:
                        - Transcribe lectures or meetings
                        - Build voice-controlled applications
                        - Create transcripts for videos and podcasts
                        - Enhance accessibility features in your apps
                        
                        Get Started:
                        - Visit the GitHub repository for detailed documentation and usage examples: 
                          https://github.com/Anubhavchaturvedi/NetHyTech-STT
                        - Watch our demo and tutorials on YouTube: 
                          https://www.youtube.com/channel/NetHyTech-STT
                        
                        Connect with Us:
                        - YouTube: https://www.youtube.com/channel/NetHyTech-STT
                        - Instagram: https://www.instagram.com/nethytech_stt
                        - Facebook: https://www.facebook.com/nethytech_stt
                        
                        License: MIT License
                        
                        ''',
    long_description_content_type='text/plain',
    url='https://github.com/Anubhavchaturvedi/NetHyTech-STT',
    project_urls={
        'Documentation': 'https://github.com/Anubhavchaturvedi/NetHyTech-STT/wiki',
        'Source Code': 'https://github.com/Anubhavchaturvedi/NetHyTech-STT',
        'Demo Video': 'https://www.youtube.com/channel/NetHyTech-STT'
    },
    packages=find_packages(),
    install_requires=[
        'selenium',
        'webdriver_manager',
    ],
    entry_points={
        'console_scripts': [
            'NetHyTech-STT = my_package.main:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
