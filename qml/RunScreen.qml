import QtQuick
import views

Rectangle {
    color: "#f0f0f0"
    
    RailView {
        anchors.fill: parent
    }
    
    Text {
        text: "Run Screen Active"
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        font.pixelSize: 20
    }
}
