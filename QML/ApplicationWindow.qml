import QtQuick 2.0
import QtQuick.Controls 2.3
import QtQuick.Controls.Universal 2.0
import QtQuick.Layouts 1.3

/*
Color Pallete - Light to Dark
1.  #F8F8F7
2.  #CFCDD7
3.  #A09DB0
4.  #89818D
5.  #5B5A62
6.  #D7CABD
  */

ApplicationWindow {
    id: start_window
    title: "WLED-Entertainment"
    visible: true
    width: 480
    height: 740
    color: "#cfcdd7"

    property QtObject obj;

    GridLayout {
        rowSpacing: 0
        rows: 4
        columns: 1
        anchors.fill: parent

        Rectangle {
            id: rectangle
            width: 200
            height: 100
            color: "#ffffff"
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            Layout.row: 1
        }

        Rectangle {
            id: rectangle2
            width: 200
            height: 100
            color: "#ffffff"
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            Layout.row: 3
        }

        Rectangle {
            id: rectangle3
            width: 200
            height: 100
            color: "#ffffff"
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            Layout.row: 4
        }

        ColumnLayout {
            id: columnLayout
            width: 480
            height: 100
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            Layout.row: 2
            Button {
                id: startButton
                text: qsTr("Start")

                contentItem: Text {
                    text: startButton.text
                    font: startButton.font
                    color: "#F8F8F7"
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    elide: Text.ElideRight
                }

                background: Rectangle  {
                    implicitWidth: 100
                    implicitHeight: 40
                    opacity: enabled ? 1 : 0.3
                    color: startButton.down ? "#d7cabd" : "#5b5a62"
                    border.color: "#d7cabd"
                    border.width: 6
                    radius: 10
                }
            }

            Button {
                id: devicesButton
                text: qsTr("Manage Devices")

                contentItem: Text {
                    text: devicesButton.text
                    font: devicesButton.font
                    color: "#F8F8F7"
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    elide: Text.ElideRight
                }

                background: Rectangle  {
                    implicitWidth: 100
                    implicitHeight: 40
                    opacity: enabled ? 1 : 0.3
                    color: devicesButton.down ? "#d7cabd" : "#5b5a62"
                    border.color: "#d7cabd"
                    border.width: 6
                    radius: 10
                }

                onClicked: {
                    if(!obj) {
                        obj = Qt.createComponent("SelectDevices.qml").createObject();
                    }
                    obj.show();
                    dataToUI.startDevicesDiscovery();
                }
            }

            Button {
                id: exitButton
                text: qsTr("Exit")

                contentItem: Text {
                    text: exitButton.text
                    font: exitButton.font
                    color: "#F8F8F7"
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    elide: Text.ElideRight
                }

                background: Rectangle  {
                    implicitWidth: 100
                    implicitHeight: 40
                    opacity: enabled ? 1 : 0.3
                    color: exitButton.down ? "#d7cabd" : "#5b5a62"
                    border.color: "#d7cabd"
                    border.width: 6
                    radius: 10
                }
            }
        }
    }

    Connections {
        target: dataToUI

    }
}
