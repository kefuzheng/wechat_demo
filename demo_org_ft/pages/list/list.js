const app = getApp()
var first = true
Page({
  data: {
    users: []
  },
  
  onLoad: function (e) {
    if (first) 
    {
      var self = this
      wx.request({
        url: app.url + '/list',
        method: 'GET',
        success: function(res) {
          var jsonData = JSON.parse(res.data)
          console.log(jsonData)
          self.setData({
            users: jsonData
          })
        }
      })
    }
  },
  delete: function(e) {
    var self = this
    wx.showModal({
      title: '提示',
      content: '是否删除该信息',
      success: function(res){
        var id = e.currentTarget.dataset.id
        var index = e.currentTarget.dataset.index
        var users = self.data.users
        users.splice(index, 1)
        
        self.setData({
          users:users
        })

        wx.request({
          url: app.url + '/delete/' + id,
          method: 'GET',
          success: function (res) {
            first = false
            // self.onLoad()
          }
        })
        }
    })
  }
})