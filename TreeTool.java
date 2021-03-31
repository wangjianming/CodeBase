package tools;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class TreeTool {


    public static TreeNode arrayToTree(Integer[] array){
        if (array.length == 0) {
            return null;
        }

        Queue<Integer> src = new LinkedList<>(Arrays.asList(array));
        TreeNode root = new TreeNode(src.remove());
        Queue<TreeNode> nodeQueue = new LinkedList<>();
        nodeQueue.add(root);


        while(!nodeQueue.isEmpty())
        {
            TreeNode node = nodeQueue.remove();
            if(!src.isEmpty())
            {
                Integer num1 = src.remove();
                if(num1 != null){
                    TreeNode node1 = new TreeNode(num1);
                    node.left = node1;
                    nodeQueue.add(node1);
                }

            }
            if(!src.isEmpty())
            {

                Integer num2 = src.remove();
                if(num2 != null){
                    TreeNode node2 = new TreeNode(num2);
                    node.right = node2;
                    nodeQueue.add(node2);
                }
            }

        }

        return root;
    }

    public static String treeNodeToString(TreeNode root) {
        if (root == null) {
            return "[]";
        }

        String output = "";
        Queue<TreeNode> nodeQueue = new LinkedList<>();
        nodeQueue.add(root);
        while(!nodeQueue.isEmpty()) {
            TreeNode node = nodeQueue.remove();

            if (node == null) {
                output += "null, ";
                continue;
            }

            output += String.valueOf(node.val) + ", ";
            nodeQueue.add(node.left);
            nodeQueue.add(node.right);
        }
        return "[" + output.substring(0, output.length() - 2) + "]";
    }

    public static void prettyPrintTree(TreeNode node, String prefix, boolean isLeft) {
        if (node == null) {
            System.out.println("Empty tree");
            return;
        }

        if (node.right != null) {
            prettyPrintTree(node.right, prefix + (isLeft ? "│   " : "    "), false);
        }

        System.out.println(prefix + (isLeft ? "└── " : "┌── ") + node.val);

        if (node.left != null) {
            prettyPrintTree(node.left, prefix + (isLeft ? "    " : "│   "), true);
        }
    }

    public static void prettyPrintTree(TreeNode node) {
        prettyPrintTree(node,  "", true);
    }

    public static void main(String[] argvs)
    {
        TreeNode tree = arrayToTree(new Integer[]{3,9,20,null,null,15,7});
        prettyPrintTree(tree);

        prettyPrintTree(arrayToTree(new Integer[]{1,2,2,3,4,4,3}));
    }

}
