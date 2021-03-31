from setuptools import setup, find_packages
   
setup(
        name= 'dancingbot_python',
        version='0.1', 
        long_description_content_type='text/markdown',
        description='use dancingbot in python pacakge',
        author='applenongbu(TNB alba)',
        author_email= 'daefrica@kakao.com', 
        url='https://github.com/applenongbu/dancingbot_python', # github url
        download_url        = 'https://github.com/applenongbu/dancingbot_python/archive/master.zip', # release 이름
        install_requires    =  ["pyserial"], # 패키지 사용시 필요한 모듈
        packages            = find_packages(exclude = []),
        keywords            = ['dancingbot_python'], # 키워드
        python_requires     = '>=3.6', # python 필요 버전
        package_data        = {}, 
        zip_safe            = False,
        classifiers         = [   
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7'
            
        ],
    )
