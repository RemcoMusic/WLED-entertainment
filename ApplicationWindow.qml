import QtQuick 2.0
import QtQuick.Controls 2.3
import QtQuick.Controls.Universal 2.0
import QtCharts 2.0
import QtQuick.Layouts 1.3


ApplicationWindow {
    id: start_window
    title: "WLED-Entertainment"
    width: 960
    height: 720
    visible: true

    GridLayout {
        rows: 3
        columns: 3
        anchors.fill: parent

        Button {
            id: startButton
            text: qsTr("Start")
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            Layout.column: 2
            Layout.row: 1

            contentItem: Text {
                text: startButton.text
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
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
            Layout.topMargin: 0
            Layout.fillWidth: false
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            Layout.column: 2
            Layout.row: 2

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

    Connections {
        target: dataToUI

    }
}
