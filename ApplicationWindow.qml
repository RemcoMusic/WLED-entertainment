import QtQuick 2.0
import QtQuick.Controls 2.3
import QtQuick.Controls.Universal 2.0

ApplicationWindow {
    id: start_window
    title: "WLED-Entertainment"
    width: 960
    height: 720
    visible: true

    Rectangle {
        id: rectangle
        width: 200
        height: 400
        color: "#A7003C"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        radius: 10

        Row {
            id: row
            x: 220
            y: 40
            width: 200
            height: 400
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            clip: false
            spacing: 0
            layoutDirection: Qt.LeftToRight

            Button {
                id: startButton
                text: qsTr("Start")
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 180
                anchors.top: parent.top
                anchors.topMargin: 180
                anchors.horizontalCenter: parent.horizontalCenter

                contentItem: Text {
                             text: startButton.text
                             font: startButton.font
                             color: "#333333"
                             horizontalAlignment: Text.AlignHCenter
                             verticalAlignment: Text.AlignVCenter
                             elide: Text.ElideRight
                         }

                background: Rectangle  {
                             implicitWidth: 100
                             implicitHeight: 40
                             opacity: enabled ? 1 : 0.3
                             color: startButton.down ? "#999999" : "#EFEFEF"
                             border.color: "#999999"
                             border.width: 3
                             radius: 10
                         }
            }

            Button {
                id: exitButton
                text: qsTr("Exit")
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.top: startButton.bottom
                anchors.topMargin: 30

                contentItem: Text {
                             text: exitButton.text
                             font: exitButton.font
                             color: "#333333"
                             horizontalAlignment: Text.AlignHCenter
                             verticalAlignment: Text.AlignVCenter
                             elide: Text.ElideRight
                         }

                background: Rectangle  {
                             implicitWidth: 100
                             implicitHeight: 40
                             opacity: enabled ? 1 : 0.3
                             color: exitButton.down ? "#999999" : "#EFEFEF"
                             border.color: "#999999"
                             border.width: 3
                             radius: 10
                         }
            }
        }
       }

}
