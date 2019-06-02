@app.route('/post', methods=['POST'])
def save_article():
   url = request.form['url_give']
   comment = request.form['comment_give']

   # 크롤링을 해서 썸네일 이미지, 타이틀, 설명을 가져옵니다
   # 나중에 짜기로 하고, 일단은 문자열로 박아둡시다!

   url_image = '썸네일 이미지 주소'
   url_title = '썸네일 타이틀'
   url_description = '썸네일 설명'

   db.article.insert_one({'url': url,'comment': comment,'image':url_image,'title':url_title,'desc':url_description})

   return jsonify({'result':'success'})

@app.route('/post', methods=['GET'])
    def get_article():
    	return jsonify({'result':'success','cards':list(db.article.find({},{'_id':False}))})


