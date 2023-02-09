import React from 'react';
import { useDispatch } from "react-redux";
import { deleteNaver } from 'webcrawler/reducers/naver.reducer';


const Naver = ({ naver, text }) => {

	const dispatch = useDispatch();
	const onClick=e=>{
		e.preventDefault()
		dispatch(deleteNaver({naver: naver}))}

	return (
		<li className="task-item">
				{naver} | {text}
				<button className="remove-task-button" onClick={onClick}>Delete</button>
		</li>
	);
};

export default Naver